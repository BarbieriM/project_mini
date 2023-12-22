from infrastructure.database_controllers.database_controller_postgres import DatabaseControllerPostgres
from domain.services.factories import DatabaseControllerFactory
from domain.services.controllers import DatabaseController
import psycopg


class DatabaseControllerFactoryPostgrees(DatabaseControllerFactory):
    def __init__(self, connection: psycopg.connect) -> None:
        self.connection = connection

    def call(self) -> DatabaseController:
        cursor = self.connection.cursor()
        return DatabaseControllerPostgres(cursor)