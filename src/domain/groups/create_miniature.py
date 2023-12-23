from domain.models import Miniature
from domain.usecases.get_database_controller import GetDatabaseController
from infrastructure.core_dependency_injection_factories.core_dependency_injection_factory_postgres import CoreDependencyInjectionFactoryJson
from src.infrastructure.core_bridge_adapters import CoreBridgeAdapter
from domain.usecases import GetInjection

def create_miniature_group(id: int, image:str, name:str, type:str, size:str,)->Miniature:
    core_dependency_injection_factory = CoreDependencyInjectionFactoryJson()
    core_bridge = CoreBridgeAdapter()

    get_injection = GetInjection(
        core_bridge, core_dependency_injection_factory
    )

    injection = get_injection.call()
    database_controller = GetDatabaseController(
        injection.database_connection_factory
    )

    database_controller = database_controller.call()

    database_controller.execute()

    


