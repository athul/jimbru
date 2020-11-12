from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from base64 import b64decode
from pydantic import BaseModel, HttpUrl
from typing import Dict
from deta import Deta
from collections import Counter
import os
import json
import dateutil
from jinja2 import Template
from datetime import datetime, date, timedelta

app = FastAPI()
db = Deta().Base()

BEACON: str = b64decode("R0lGODlhAQABAIAAANvf7wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==")

DOMAIN: str = "http://127.0.0.1:9000"
TITLE:str = "Notes Site"
JS: str = """(function(){
    var d=document,i=new Image,e=encodeURIComponent;
    i.src='%s/a.gif?url='+e(d.location.href)+'&ref='+e(d.referrer);
    })()""".replace(
    "\n", ""
)


class URL(BaseModel):
    url: HttpUrl


class Pageviews(BaseModel):
    url: str
    ip: str
    referrer: str
    headers: dict
    day: str
    time: str
    hour: str


@app.get("/page")
def getDom(url: HttpUrl, request: Request):
    now = datetime.now()
    day = now.strftime("%B %d, %Y")
    time = now.strftime("%H:%M:%S")
    return date.today()


@app.get("/a.gif")
def getImg(request: Request):
    pushtoDB(request)
    return Response(
        content=BEACON,
        media_type="img/gif",
        headers={"Cache-Control": "private, no-cache"},
    )


@app.get("/a.js")
def getJs():
    return Response(content=JS % DOMAIN, media_type="text/javascript")


def pushtoDB(req: Request) -> Dict:
    url = URL(url=req.query_params["url"])
    if "localhost" or "127.0.0.1" in url.url.host:
        return {"msg": "no-data pushed"}
    ip = req.client.host
    now = datetime.now()
    referrer = req.query_params["ref"] or ""
    headers = dict(req.headers)
    data = Pageviews(
        url=f"{url.url.host}{url.url.path}",
        ip=ip,
        referrer=referrer,
        headers=headers,
        day=date.today().strftime("%Y/%m/%d"),
        time=now.strftime("%B %d, %Y %H:%M:%S"),
        hour=now.strftime("%H"),
    )
    db.put(vars(data))
    return vars(data)


@app.get("/hits")
def getHitsPerDay():
    today = date.today()
    hits = []
    days = []
    for i in range(0, 7):
        day = (today - timedelta(days=i)).strftime("%Y/%m/%d")
        days.append(day)
        day_hits = db.fetch({"day": day})
        hits.append(len(next(day_hits)))
    return days[::-1], hits[::-1]


def getAllthings() -> Dict:
    data = next(db.fetch())
    refs = []
    urls = []
    hours = []
    visIpList =[]
    for datum in data:
        refs.append(datum["referrer"])
        urls.append(datum["url"])
        hours.append(datum["hour"])
        visIpList.append(datum['ip'])
    refListCleaned = list(Counter(refs).keys())
    refListNos = list(Counter(refs).values())
    urlListCleaned = list(Counter(urls).keys())
    urlHitNos = list(Counter(urls).values())
    HourListCleaned = list(Counter(hours).keys())
    HourHitNos = list(Counter(hours).values())
    ipListCleaned = list(Counter(visIpList).keys())
    ipHitNos = list(Counter(visIpList).values())
    ipDict = {ipListCleaned[i]:ipHitNos[i] for i in range(len(ipListCleaned))}
    refDict = {refListCleaned[i]: refListNos[i] for i in range(len(refListCleaned))}
    urlHitDict = {urlListCleaned[i]: urlHitNos[i] for i in range(len(urlListCleaned))}
    refSortDict = {
        k: v for k, v in sorted(refDict.items(), key=lambda item: item[1], reverse=True)
    }
    urlHitSortDict = {
        k: v for k, v in sorted(urlHitDict.items(), key=lambda item: item[1], reverse=True)
    }
    ipHitSortDict ={
        k:v for k, v in sorted(ipDict.items(), key=lambda item: item[1], reverse=True)
    }
    print(refSortDict)
    return refSortDict, urlHitSortDict, HourListCleaned, HourHitNos, ipHitSortDict


@app.get("/")
def renderIndex():
    baseTemp = Template(open("index.html").read())
    days, hits = getHitsPerDay()
    refs, hiturls, hours, hhits,ips = getAllthings()
    return HTMLResponse(
        baseTemp.render(
            title=TITLE,hitarr=hits, days=days, refs=refs, urls=hiturls, hours=hours, hhits=hhits,ip=ips
        )
    )
