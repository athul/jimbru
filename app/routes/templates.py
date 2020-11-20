from .analytics import router
from .helpers import getHitsPerDay, getAllthings
from .filters import flagize,hmantime,getConutryCode
from datetime import datetime
from jinja2 import Template
from .analytics import TITLE
from .auth import manager
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Request,Depends,security
from os import path

router = APIRouter()

pth = path.dirname(__file__)
templates = Jinja2Templates(directory=path.join(pth, "templates"))
templates.env.filters['flagize'] = flagize
templates.env.filters['dateit'] = hmantime
templates.env.filters['getctCode'] = getConutryCode


@router.get("/dash",response_class=HTMLResponse)
def renderIndex(request: Request,user=Depends(manager)):
    print(user)
    js = Template(open(path.join(pth, "templates/chart.js")).read())
    days, hits = getHitsPerDay()
    refs, hiturls, hours, hhits, iptime,totHits,os,browsers,dev,lt,ctDict = getAllthings()
    print(refs, "----\n----",hiturls, "----\n----",hours, "----\n----",hhits, "----\n----",iptime,"----\n----",totHits,"----\n----",os,"----\n----",browsers,"----\n----",dev,"----\n----",lt,"----\n----",ctDict,"---\n---",days,"---\n---",hits )
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
@router.get("/sess/{time}",response_class=HTMLResponse)
def getVisitorDetails(req:Request,time:str,user=Depends(manager)):
    ip,urlsIP = getAllthings(True)
    trdict =[]
    ipSorted = sorted(ip, key=lambda k: sorted(k.keys()), reverse=True)
    urlSorted = sorted(urlsIP, key=lambda k: sorted(k.keys()), reverse=True)
    for data in ipSorted:
        if data.get(time):
            for udict in urlSorted:
                if udict.get(data[time]['ip']):
                    trdict.append(udict)
                    print("Trdict",trdict)
            trSortdict = sorted(trdict,key=lambda key:key.get(data[time]['ip'])['time'],reverse=True)
            return templates.TemplateResponse("session.html",{"request": req,"ipdata":data,"hitdata":trSortdict})

@router.get("/",response_class=HTMLResponse)
def loginwithCreds(request:Request):
    with open(path.join(pth, "templates/login.html")) as f:
        return HTMLResponse(content=f.read())