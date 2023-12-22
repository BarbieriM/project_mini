from infrastructure.database_controller_factories.database_controller_factory_postgres import DatabaseControllerFactoryPostgrees
from infrastructure.database_controllers.database_controller_postgres import DatabaseControllerPostgres

from domain.models import DependencyInjection, Injection
from domain.services.controllers import *
from domain.services.controllers import *

class CoreBridge:
    def __init__(self):
        self.adapters = {
            "database_controller_postgres": DatabaseControllerPostgres(),
            "database_controller_factory_postgres": DatabaseControllerFactoryPostgrees(),
        }
    def get_injection(self, dependency_injection:DependencyInjection)-> Injection:
        return Injection(
            self.adapters[dependency_injection.database_controller],
            self.adapters[dependency_injection.database_controller_factory]
        )