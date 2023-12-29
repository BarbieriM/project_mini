from domain.models import Miniature
from domain.usecases.get_database_controller import GetDatabaseController
from infrastructure.core_dependency_injection_factories.core_dependency_injection_factory_postgres import CoreDependencyInjectionFactoryJson
from infrastructure.core_bridge_adapters import CoreBridgeAdapter
from domain.usecases import GetInjection
import uuid
import json
from infrastructure.miniature_factories.miniature_factory_json import MiniatureFactoryJson
from domain.usecases import CreateMiniature
from infrastructure.miniature_repositories.miniature_repository_postgres import MiniatureRepositoryPostgres


def create_miniature_group() -> Miniature:
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
    # get database controller recebe uma instancia de
    #  connect database factory que esta definido no injection

    database_controller = database_controller.call()

    new_mini = CreateMiniature(
        injection.miniature_factory_json
    )
# gambiarr
    with open(
        "C:\\Users\\Mateus\\dev\\project_mini\\utils\\mini_test.json",
        "r",
    ) as f:
        miniature_info = json.load(f)

    miniature = new_mini.call(uuid.uuid1, miniature_info.image, miniature_info.name, miniature_info.type, miniature_info.size)
    # miniature = MiniatureFactoryJson()
# fazer um usecase para criar miniatura que recebe um instancia de miniature factory como parametro e tenho que colocar no core bridge adapter e nas injectrions q sera usado o json

    miniature_repository = MiniatureRepositoryPostgres()
    return miniature_repository.create_miniature(
        miniature, database_controller)
