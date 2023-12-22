from domain.services.repositories.user_repository import UserRepository
from domain.models.user import User
from domain.services.controllers.database_controller import DatabaseController


class UserRepositoryPostgres(UserRepository):
    def create_user(self, user: User, database_controller: DatabaseController):
        database_controller.execute("INSERT INTO users (id, user_name, user_email) VALUES (%s)", (user, ))


    def get_user_by_email(self, user_email: str, database_controller: DatabaseController) -> User:
        user = database_controller.execute("SELECT user where user_email = %s", (user_email, ))
        return User(**user)