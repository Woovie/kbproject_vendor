import uuid

class ScraperObject():
    def __init__(self):
        pass

    def set_id(self, namespace_uuid: uuid.UUID, name: str):
        self.uuid = uuid.uuid5(namespace_uuid, name)