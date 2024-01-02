from domain.models import Miniature
from domain.services.factories.miniature_factory import MiniatureFactory


class CreateMiniature:
    def __init__(
            self,
            miniature_factory: MiniatureFactory,
    ):
        self.miniature_factory = miniature_factory

    def call(self, image: str, name: str, type: str, size: str) -> Miniature:
        return self.miniature_factory.call( image, name, type, size)
