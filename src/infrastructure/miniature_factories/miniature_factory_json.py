from domain.models import Miniature
from domain.services.factories import MiniatureFactory
import uuid
import json
import os


class MiniatureFactoryJson(MiniatureFactory):
    def call(self, image: str, name: str, type: str, size: str) -> Miniature:
        miniature_file = open(name, "r",)
        miniature = json.load(miniature_file)

        return Miniature(
            uuid.uuid1(), 
            miniature["image"], 
            miniature["name"], 
            miniature["type"], 
            miniature["size"],
        )
