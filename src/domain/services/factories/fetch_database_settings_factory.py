from domain.models import DatabaseSettings

class FetchDatabaseSettingsFactory:
    def call(self, path)-> DatabaseSettings:
        raise NotImplementedError()