from vendor import baseclass
import uuid

class Option(baseclass.BaseClass):
    def __init__(self):
        pass

    def create_option(self, option_type: str):#TODO: Add some type hinting for returning a... class? particular class type?
        if (option_type == "Shopify"):
            option = ShopifyOption()
        return option

    def build_name(self):
        pass

    def build_price(self):
        pass

    def build_availability(self):
        pass

    def build_pre(self):
        pass

    def build_post(self):
        pass

    def build(self):
        self.build_pre()
        self.build_name()
        self.build_price()
        self.build_availability()
        self.build_post()
        return self

class ShopifyOption(Option):
    def set_data(self, payload: dict):
        self.json = payload

    def set_featured_image(self, namespace_uuid: uuid.UUID):
        if self.json['featured_image']:
            self.image = uuid.uuid5(namespace_uuid, self.json['featured_image']['src'])

    def build_name(self):
        self.name = self.json["title"]

    def build_price(self):
        self.price = self.json["price"]

    def build_availability(self):
        self.available = self.json["available"]
