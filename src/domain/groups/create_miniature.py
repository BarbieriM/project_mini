from domain.models import Miniature
from domain.usecases.get_database_controller import GetDatabaseController
from infrastructure.core_dependency_injection_factories.core_dependency_injection_factory_postgres import CoreDependencyInjectionFactoryJson
from src.infrastructure.core_bridge_adapters import CoreBridgeAdapter
from domain.usecases import GetInjection

def create_miniature_group(id: int, image:str, name:str, type:str, size:str,)->Miniature:
    core_dependency_injection_factory = CoreDependencyInjectionFactoryJson()
    # todas as dependencias do json
    # se eu quiser eu posso deixar isso em aberto para alterar para uma api externa ou para um .envrc?

    core_bridge = CoreBridgeAdapter()
    # importa o core bridge adapter como uma classe que retorna uma injection

    get_injection = GetInjection(
        core_bridge, core_dependency_injection_factory
    )
    # o retorno da funcao call do  GetInjection retorna o chamado de get 
    # injection do core bridge adapter 
    # e as c

    injection = get_injection.call()
    # retorna as injections
    database_controller = GetDatabaseController(
        injection.database_connection_factory
    )

    database_controller = database_controller.call()

    database_controller.execute()
