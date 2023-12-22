from dataclasses import dataclass

@dataclass
class DatabaseSettings:
    user:str
    port:int
    password:str
    host:str
    database_name:str
