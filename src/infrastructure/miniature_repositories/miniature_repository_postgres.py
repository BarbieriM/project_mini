from domain.services.repositories.miniature_repository import MiniatureRepository
from domain.models import Miniature
from domain.services.controllers.database_controller import DatabaseController


class MiniatureRepositoryPostgres(MiniatureRepository):
    def create_miniature(self, miniature:Miniature, database_controller: DatabaseController)->Miniature:
        database_controller.execute("INSERT INTO miniatures (id, image, name, size, type) VALUES (%s)", (miniature, ))

        # devo colocar os parametros de Miniature ou a dataclass Miniature em si? afinal eu to retornando um Miniature

    def get_all_miniatures(self, database_controller: DatabaseController) -> list[Miniature]:
        miniatures = database_controller.execute("SELECT * from miniatures")
        return [Miniature(**miniature_data) for miniature_data in miniatures]