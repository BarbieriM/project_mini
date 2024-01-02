from domain.models import DatabaseSettings
from domain.services.factories import FetchDatabaseSettingsFactory
import json

class FetchDatabaseSettingsFactoryJson(FetchDatabaseSettingsFactory):
    def call(self, path)->DatabaseSettings:
        database_file = open(path, "r",)
        database_settings = json.load(database_file)
        return DatabaseSettings(
            database_settings["user"],
            database_settings["port"],
            database_settings["password"],
            database_settings["host"],
            database_settings["database_name"]
        )