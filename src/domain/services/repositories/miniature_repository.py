from domain.services.controllers.database_controller import DatabaseController
from domain.models import Miniature

class MiniatureRepository:
    def create_miniature(self, miniature: Miniature, database_controller: DatabaseController):
        raise NotImplementedError()
    
    def get_miniature(self, name: str, database_controller: DatabaseController) -> Miniature:
        raise NotImplementedError()
    
    def get_all_miniatures(self, database_controller:DatabaseController)->list[str]:
        raise NotImplementedError()