from domain.models.database_settings import DatabaseSettings
from domain.services.factories import FetchDatabaseSettingsFactory


class GetDatabaseSettings:
    def __init__(self, fetch_database_settings_factory:FetchDatabaseSettingsFactory):
        self.fetch_database_settings_factory = fetch_database_settings_factory

    def call(self, path)-> DatabaseSettings:
        return self.fetch_database_settings_factory.call(path)