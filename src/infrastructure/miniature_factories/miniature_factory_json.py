from domain.models import Miniature
from domain.services.factories import MiniatureFactory
import uuid
import json


class MiniatureFactoryJson(MiniatureFactory):
    def call(self, id: str, image: str, name: str, type: str, size: str) -> Miniature:
        # with open(
        #     "C:\Users\Mateus\dev\project_mini\utils\mini_test.json",
        #     "r",
        # ) as f:
        #     miniature = json.load(f)
        return Miniature(
            id, 
            image, 
            name, 
            type, 
            size
        )
