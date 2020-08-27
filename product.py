from vendor import baseclass, option, image
import configparser

class Product(baseclass.BaseClass):# product = Product(config).create_product("Shopify")
    def __init__(self):
        pass

    def create_product(self, product_type: str):#TODO: Look at option file type hinting, also do it here.
        if (product_type == "Shopify"):
            product = ShopifyProduct()
        return product

    def build_name(self):
        pass

    def build_uri(self):
        pass

    def build_images(self):
        pass

    def build_pre(self):
        pass

    def build_post(self):
        pass

    def build(self):
        self.build_pre()
        self.build_name()
        self.build_uri()
        self.build_images()
        self.build_post()

class ShopifyProduct(Product):# Factory
    def build_name(self):
        self.name = self.json["title"]

    def build_uri(self):
        self.uri = f"{self.config['shopify']['product_prefix']}{self.json['handle']}"

    def build_images(self):
        self.images = []
        for image in self.json["images"]:
            self.images.append(self.build_image(image))

    def build_image(self, image: dict) -> image.Image:
        image_object = image.Image(image["src"])
        image_object.set_id(self.uuid, image_object.url)
        return image_object.build()

    def build_variants(self):
        self.variants = []
        for variant in self.json["variants"]:
            self.variants.append(self.build_variant(variant))

    def build_variant(self, variant: dict) -> option.Option:
        option_object = option.ShopifyOption()
        option_object.set_data(variant)
        option_object.set_featured_image(self.uuid)
        option_object.build()
        option_object.set_id(self.uuid, option_object.name)
        return option_object

    def set_data(self, config: configparser.ConfigParser, payload: dict):
        self.config = config
        self.json = payload

    def build_post(self):
        self.build_variants()