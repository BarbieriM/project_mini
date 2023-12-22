import json
from domain.models import DependencyInjection
from domain.services.factories import CoreDependencyInjectionFactory


class CoreDependencyInjectionFactoryJson(CoreDependencyInjectionFactory):
    def call(self) -> DependencyInjection:
        with open(
            "C:\Users\enzob\dev\devrise\project-mini\api\utils\dependency_injection.json",
            "r",
        ) as f:
            dependency_injections = json.load(f)
            return DependencyInjection(
                dependency_injections["database_controller_factory"],
                dependency_injections["database_connection_factory"],
                dependency_injections["database_controller"],
            )
