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


class RedirectService(BaseModel):
    external_name: str
    redirect: str


class Service(BaseModel):
    external_name: str
    proxied: ProxiedService | str
    websocket_path: Optional[str] = None
    additional_headers: dict[str, str] = Field(default_factory=dict)
    additional_options: list[str] = Field(default_factory=list)


AnyService = Service | RedirectService


class WholeConfig(BaseModel):
    global_: Global = Field(alias="global")
    services: list[AnyService]


def parse_yaml(data: str) -> WholeConfig:
    return WholeConfig(**yaml.safe_load(data))
