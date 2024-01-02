from domain.models import Miniature
from domain.usecases.get_database_controller import GetDatabaseController
from domain.usecases.get_database_settings import GetDatabaseSettings
from infrastructure.core_dependency_injection_factories.core_dependency_injection_factory_postgres import CoreDependencyInjectionFactoryJson
from infrastructure.core_bridge_adapters import CoreBridgeAdapter
from domain.usecases import GetInjection
from infrastructure.miniature_factories.miniature_factory_json import MiniatureFactoryJson
from domain.usecases import CreateMiniature
from infrastructure.miniature_repositories.miniature_repository_postgres import MiniatureRepositoryPostgres


def create_miniature_group() -> Miniature:
    core_dependency_injection_factory = CoreDependencyInjectionFactoryJson()
    # todas as dependencias do json
    # se eu quiser eu posso deixar isso em aberto para alterar para uma api externa ou para um .envrc?

    database_settings_path = "C:\\Users\\enzob\\dev\\devrise\\project-mini\\api\\utils\\database_settings.json"
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

    get_database_settings = GetDatabaseSettings(injection.fetch_database_settings_factory)

    database_settings = get_database_settings.call(database_settings_path)

    database_controller = GetDatabaseController(
        injection.database_connection_factory
    )
    # get database controller recebe uma instancia de
    #  connect database factory que esta definido no injection

    print(database_settings)
    # breakpoint()

    database_controller = database_controller.call(database_settings)


    new_mini = CreateMiniature(
        injection.miniature_factory
    )
    
    miniature = new_mini.call("", "C:\\Users\\enzob\\dev\\devrise\\project-mini\\api\\utils\\mini_test.json", "", "")
    # miniature = MiniatureFactoryJson()
    # miniature.call("", "C:\\Users\\Mateus\\dev\\project_mini\\utils\\mini_test.json", "", "")
    # fazer um usecase para criar miniatura que recebe um instancia de miniature factory como parametro e tenho que colocar no core bridge adapter e nas injectrions q sera usado o json

    miniature_repository = MiniatureRepositoryPostgres()
    return miniature_repository.create_miniature(
        miniature, database_controller)
