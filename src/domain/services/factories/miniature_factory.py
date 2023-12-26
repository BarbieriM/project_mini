from domain.models.miniature import Miniature


class MiniatureFactory:
    def call(self, id, image, name, type, size)->Miniature:
        raise NotImplementedError