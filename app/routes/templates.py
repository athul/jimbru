from .analytics import router
from .helpers import getHitsPerDay, getAllthings
from .filters import flagize,hmantime,getConutryCode
from datetime import datetime
from jinja2 import Template
from .analytics import TITLE
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Request
from os import path

router = APIRouter()

pth = path.dirname(__file__)
templates = Jinja2Templates(directory=path.join(pth, "templates"))
templates.env.filters['flagize'] = flagize
templates.env.filters['dateit'] = hmantime
templates.env.filters['getctCode'] = getConutryCode


@router.get("/")
def renderIndex(request: Request):
    js = Template(open(path.join(pth, "templates/chart.js")).read())
    days, hits = getHitsPerDay()
    refs, hiturls, hours, hhits, iptime,totHits,os,browsers,dev,lt,ctDict = getAllthings()
    ipSorted = sorted(iptime, key=lambda k: sorted(k.keys()), reverse=True)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "title": TITLE,
        "loadTime":lt,
        "tothits":totHits,
        "refs": refs,
        "urls": hiturls,
        "os": os,
        "dev":dev,
        "cflg": ipSorted,
        "browser":browsers,
        "time ": ipSorted,
        "countries":ctDict,
        "chart": js.render(
            hitarr=hits, days=days, hours=hours, hhits=hhits, os=os
        ),
    },
    )

    # return nw
@router.get("/sess/{time}")
def getVisitorDetails(req:Request,time:str):
    ip = getAllthings(True)
    ipSorted = sorted(ip, key=lambda k: sorted(k.keys()), reverse=True)
    for data in ipSorted:
        if data.get(time):
            return templates.TemplateResponse("session.html",{"request": req,"ipdata":data})