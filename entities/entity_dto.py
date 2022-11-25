import json


class EntityDTO:
    def to_json(self):
        json.dumps(self.__dict__, indent=4)
