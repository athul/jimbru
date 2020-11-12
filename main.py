from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from base64 import b64decode
from pydantic import BaseModel, HttpUrl
from pytz import timezone
from typing import Dict,Optional
from deta import Deta
from collections import Counter
import os
import json
import dateutil
from jinja2 import Template
from datetime import datetime, date, timedelta

app = FastAPI()
db = Deta(os.getenv("DETA_KEY")).Base(os.getenv("DB_NAME"))

BEACON: str = b64decode("R0lGODlhAQABAIAAANvf7wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==")

DOMAIN: str = os.getenv("DOMAIN")
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
    referrer: str
    headers: dict
    day: str
    time: str
    hour: Optional[str]


@app.get("/page")
def getDom(url: HttpUrl, request: Request):
    return next(db.fetch())


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
    now = datetime.now().astimezone(timezone('Asia/Kolkata'))
    print("Host",req.client.host)
    referrer = req.query_params["ref"] or ""
    headers = dict(req.headers)
    data = Pageviews(
        url=f"{url.url.host}{url.url.path}",
        referrer=referrer,
        headers=headers,
        day=now.strftime("%Y/%m/%d"),
        time=now.strftime("%B %d, %Y %H:%M:%S"),
        hour=now.strftime("%H"),
    )
    print(now.strftime("%B %d, %Y %H:%M:%S"))
    db.put(vars(data))
    return vars(data)


@app.get("/hits")
def getHitsPerDay():
    today = datetime.now().astimezone(timezone('Asia/Kolkata'))
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
    devices = []
    android=mac=win=linux=other=phone=desktop=ios=oth_os = 0
    for datum in data:
        refs.append(datum["referrer"])
        urls.append(datum["url"])
        hours.append(datum["hour"])
        devices.append(datum['headers']['user-agent'].strip())
    for device in devices:
        if 'Macintosh' in device:
            mac+=1
            desktop+=1
        elif 'Android' in device:
            android+=1
            phone+=1
        elif "Win" in device:
            win+=1
            desktop+=1
        elif "Linux" in device:
            linux+=1
            desktop+=1
        elif "iPhone" in device:
            ios+=1
            phone+=1
        else:
            other+=1
            oth_os+=1
    os ={"Mac OS X":mac,"Linux":linux,"Windows":win,"Other":oth_os,"Android":android,"iOS":ios,}
    devc = {"Desktop":desktop,"Mobile":phone,"Other":other}
    OS = {k: v for k, v in sorted(os.items(), key=lambda item: item[1], reverse=True)}
    DEVICES = {k: v for k, v in sorted(devc.items(), key=lambda item: item[1], reverse=True)}
    refListCleaned = list(Counter(refs).keys())
    for i in range(len(refListCleaned)):
        if refListCleaned[i] == "":
            refListCleaned[i] = "Direct"
    refListNos = list(Counter(refs).values())
    urlListCleaned = list(Counter(urls).keys())
    urlHitNos = list(Counter(urls).values())
    HourListCleaned = list(Counter(hours).keys())
    HourHitNos = list(Counter(hours).values())
    refDict = {refListCleaned[i]: refListNos[i] for i in range(len(refListCleaned))}
    urlHitDict = {urlListCleaned[i]: urlHitNos[i] for i in range(len(urlListCleaned))}
    refSortDict = {
        k: v for k, v in sorted(refDict.items(), key=lambda item: item[1], reverse=True)
    }
    urlHitSortDict = {
        k: v for k, v in sorted(urlHitDict.items(), key=lambda item: item[1], reverse=True)
    }
    return refSortDict, urlHitSortDict, HourListCleaned, HourHitNos,OS,DEVICES


@app.get("/")
def renderIndex():
    baseTemp = Template(open("index.html").read())
    days, hits = getHitsPerDay()
    refs, hiturls, hours, hhits,os,dev = getAllthings()
    # print(hits)
    # refs={'https://athul.github.io/notes/all.html': 6, 'https://athul.github.io/notes/posts/git-tags.html': 1, 'https://athul.github.io/notes/posts/air-zettel.html': 1, 'https://athul.github.io/notes/': 1, 'https://athul.github.io/notes/posts/golang.html': 1, 'https://athul.github.io/notes/posts/git-cherry.html': 1}
    # hiturls={'athul.github.io/notes/posts/air-zettel.html': 4, 'athul.github.io/notes/posts/toc.html': 3, 'athul.github.io/notes/all.html': 2, 'athul.github.io/notes/posts/golang.html': 1, 'athul.github.io/notes/': 1, 'athul.github.io/notes/posts/git-tags.html': 1}
    # hours=['14', '17', '20', '13']
    # hhits=[3, 7, 1, 1]
    # days=['2020/11/06', '2020/11/07', '2020/11/08', '2020/11/09', '2020/11/10', '2020/11/11', '2020/11/12']
    # hits=[3, 5, 11, 0, 24, 0, 12]
    # os={'Mac OS X': 12, 'Linux': 0, 'Windows': 0, 'Other': 0, 'Android': 6, 'iOS': 4}
    # dev={'Desktop': 12, 'Mobile': 10, 'Other': 0}
    return HTMLResponse(
        baseTemp.render(
            title=TITLE,hitarr=hits, days=days, refs=refs, urls=hiturls, hours=hours, hhits=hhits,dev=dev,os=os
        )
    )
