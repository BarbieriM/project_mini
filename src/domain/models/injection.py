from dataclasses import dataclass

from domain.services.controllers import *
from domain.services.factories import *

@dataclass
class Injection:
    database_controller: DatabaseController
    database_controller_factory: DatabaseControllerFactory