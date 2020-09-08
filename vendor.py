import re, configparser, json, uuid, hashlib

from kbproject_vendor import baseclass, product

class Vendor(baseclass.BaseClass):
    def __init__(self, vendor_dict: dict):
        self.price_regex = re.compile(r"(\d{1,3}\,){0,3}\d{1,3}(\.\d{2})?")
        self.name = vendor_dict["name"]
        self.url = vendor_dict["url"]
        self.cms = vendor_dict["cms"]
        self.scrape = vendor_dict["scrape?"]
        self.products = []
        self.json = []

    def process_scraped_data(self):
        pass

class ShopifyVendor(Vendor):
    def set_data(self, config: configparser.ConfigParser):
        self.config = config
        self.scrape_url = f"https://{self.url}{self.config['shopify']['data_location']}"
        self.uuid = uuid.uuid5(uuid.NAMESPACE_URL, self.url)

    def process_scraped_data(self, body: str):
        self.json = json.loads(body)['products']

    def build_products(self):
        for product in self.json:
            self.products.append(self.build_product(product))
    
    def build_product(self, product_dict: dict):
        product_object = product.Product().create_product("shopify")
        product_object.set_data(self.config, product_dict)
        product_object.set_id(self.uuid, product_object.json["title"])# ID must come first as it's needed for builds that are triggered by the product itself.
        product_object.build()
        return product_object
