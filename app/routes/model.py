from pydantic import BaseModel, HttpUrl
from typing import Optional
from .settings import deta_key,deta_pname
from deta import Deta

db = Deta(deta_key).Base(deta_pname)


class URL(BaseModel):
    url: HttpUrl


class Pageviews(BaseModel):
    url: str
    referrer: str
    headers: dict
    ip: dict
    ip_addr:str
    day: str
    time: str
    device:str
    device_browser:str
    device_type:str
    os:str
    loadtime:str
    hour: Optional[str]
