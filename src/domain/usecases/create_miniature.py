from domain.models import Miniature
from domain.services.factories.create_miniature_factory import CreateMiniatureFactory

class CreateMiniature:
    def __init__(
            self,
            create_miniature_factory:CreateMiniatureFactory,
            ):
        self.create_miniature_factory = create_miniature_factory

    def call(self)-> Miniature:
        return self.create_miniature_factory.call()
