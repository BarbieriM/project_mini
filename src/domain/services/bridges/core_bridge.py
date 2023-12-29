from domain.models import DependencyInjection, Injection
from domain.services.controllers import *
from domain.services.factories import *

class CoreBridge:
    def get_injection(self, dependency_injection:DependencyInjection)->Injection:
        raise NotImplementedError()