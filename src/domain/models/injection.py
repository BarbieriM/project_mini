from dataclasses import dataclass

from domain.services.controllers import *
from domain.services.factories import *

@dataclass
class Injection:
    database_connection_factory: DatabaseControllerFactory
    # database_controller: DatabaseController
    miniature_factory: MiniatureFactory
    fetch_database_settings_factory: FetchDatabaseSettingsFactory