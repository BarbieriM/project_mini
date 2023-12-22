from domain.services.controllers.database_controller import DatabaseController


class UserRepository:
    def create_user(self, user: User, database_controller: DatabaseController):
        raise NotImplementedError()
    
    def get_user_by_email(self, user_email: str, database_controller: DatabaseController) -> User:
        raise NotImplementedError()