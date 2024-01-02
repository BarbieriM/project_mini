from domain.models.miniature import Miniature


class MiniatureFactory:
    def call(self, image: str, name: str, type: str, size: str) -> Miniature:
        raise NotImplementedError
