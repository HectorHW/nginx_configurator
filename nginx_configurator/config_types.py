from typing import Optional
from pydantic import BaseModel, Field
import yaml


class SSL(BaseModel):
    certificate_path: str
    key_path: str


class Global(BaseModel):
    hostname: str
    port_number: int = 8080
    ssl: Optional[SSL] = None


class ProxiedService(BaseModel):
    port: int
    proto: str = "http"
    host: str = "127.0.0.1"


class Service(BaseModel):
    external_name: str
    proxied: ProxiedService
    websocket_path: Optional[str] = None


class WholeConfig(BaseModel):
    global_: Global = Field(alias="global")
    services: list[Service]


def parse_yaml(data: str) -> WholeConfig:
    return WholeConfig(**yaml.safe_load(data))
