from pydantic import BaseModel, HttpUrl
from typing import Optional
from deta import Deta

db = Deta().Base()


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
