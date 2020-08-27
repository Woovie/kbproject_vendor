import re, configparser

from kbproject_vendor import baseclass, product

class Vendor(baseclass.BaseClass):
    def __init__(self):
        self.price_regex = re.compile(r"(\d{1,3}\,){0,3}\d{1,3}(\.\d{2})?")

class ShopifyVendor(Vendor):
    def set_data(self, config: configparser.ConfigParser, url: str):
        self.config = config
        self.url = url
        self.scrape_url = f"{self.url}{self.config['shopify']['data_location']}"