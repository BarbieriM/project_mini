from dataclasses import dataclass

@dataclass
class DependencyInjection:
    database_connection_factory:str
    # database_controller:str
    miniature_factory:str
    fetch_database_settings_factory:str
    