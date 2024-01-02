from infrastructure.database_connection_factories.database_connection_factory_postgres import DatabaseConnectionFactoryPostgres
from infrastructure.database_controller_factories.database_controller_factory_postgres import DatabaseControllerFactoryPostgrees
from infrastructure.database_controllers import DatabaseControllerPostgres
from infrastructure.fetch_database_settings_factories import FetchDatabaseSettingsFactoryJson
from infrastructure.miniature_factories.miniature_factory_json import MiniatureFactoryJson

from domain.models import DependencyInjection, Injection
from domain.services.controllers import *
from domain.services.controllers import *

class CoreBridgeAdapter:
    def __init__(self):
        self.adapters = {
            "database_connection_factory_postgres": DatabaseConnectionFactoryPostgres(),
            "miniature_factory_json": MiniatureFactoryJson(),
            "fetch_database_settings_factory_json" : FetchDatabaseSettingsFactoryJson(),
        }
        #se eu tivesse outros adapters pra outro tipo de banco eu iria colocar eles aqui tambem?
        #  

    def get_injection(self, dependency_injection:DependencyInjection)-> Injection:
        return Injection(
            self.adapters[dependency_injection.database_connection_factory],
            # self.adapters[dependency_injection.database_controller],
            self.adapters[dependency_injection.miniature_factory],
            self.adapters[dependency_injection.fetch_database_settings_factory],

        )