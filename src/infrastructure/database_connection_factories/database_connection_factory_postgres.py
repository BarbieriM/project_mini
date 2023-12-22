from infrastructure.database_controller_factories.database_controller_factory_postgres import DatabaseControllerFactoryPostgrees
from domain.services.factories.database_connection_factory import DatabaseConnectionFactory
from domain.services.factories.database_controller_factory import DatabaseControllerFactory
from domain.models.database_settings import DatabaseSettings

import psycopg


class DatabaseConnectionFactoryPostgres(DatabaseConnectionFactory):
    def call(database_settings: DatabaseSettings) -> DatabaseControllerFactory:
        connection = psycopg.connect(
            host=database_settings.host,
            dbname=database_settings.name,
            user=database_settings.user,
            password=database_settings.pasw,
            port=database_settings.port,
        )

        return DatabaseControllerFactoryPostgrees(connection)