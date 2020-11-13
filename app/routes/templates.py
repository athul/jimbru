from .analytics import router
from .helpers import getHitsPerDay, getAllthings,getDatafromIP,pushtoDB
from .filters import *
from datetime import datetime
from jinja2 import Template
from .analytics import TITLE
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter,Request
from os import path
import flag

router = APIRouter()

pth = path.dirname(__file__)
templates = Jinja2Templates(directory=path.join(pth, "templates"))
templates.env.filters['flagize']=flagize
templates.env.filters['dateit'] = hmantime

@router.get("/")
def renderIndex(request:Request):
    js = Template(open(path.join(pth, "templates/chart.js")).read())

    days,hits = getHitsPerDay()
    refs, hiturls, hours, hhits,os,dev,iptime = getAllthings()
    ipSorted=sorted(iptime, key=lambda k: k['time'],reverse=True) 
    # ipSorted=[{'time':'2020-11-13 20:44:50.228370+05:30','ip' :{'asn': 'AS38266', 'city': 'Trivandrum', 'continent_code': 'AS', 'country': 'IN', 'country_area': 3287590, 'country_calling_code': '+91', 'country_capital': 'New Delhi', 'country_code': 'IN', 'country_code_iso3': 'IND', 'country_name': 'India', 'country_population': 1352617328, 'country_tld': '.in', 'currency': 'INR', 'currency_name': 'Rupee', 'in_eu': False, 'ip': '1.39.78.203', 'languages': 'en-IN,hi,bn,te,mr,ta,ur,gu,kn,ml,or,pa,as,bh,sat,ks,ne,sd,kok,doi,mni,sit,sa,fr,lus,inc', 'latitude': 8.4855, 'longitude': 76.9492, 'org': 'Vodafone India Ltd.', 'postal': '695021', 'region': 'Kerala', 'region_code': 'KL', 'timezone': 'Asia/Kolkata', 'utc_offset': '+0530', 'version': 'IPv4'}}, {'time':'2020-11-13 20:49:46.506089+05:30','ip':{'asn': 'AS38266', 'city': 'Trivandrum', 'continent_code': 'AS', 'country': 'IN', 'country_area': 3287590, 'country_calling_code': '+91', 'country_capital': 'New Delhi', 'country_code': 'IN', 'country_code_iso3': 'IND', 'country_name': 'India', 'country_population': 1352617328, 'country_tld': '.in', 'currency': 'INR', 'currency_name': 'Rupee', 'in_eu': False, 'ip': '1.39.78.203', 'languages': 'en-IN,hi,bn,te,mr,ta,ur,gu,kn,ml,or,pa,as,bh,sat,ks,ne,sd,kok,doi,mni,sit,sa,fr,lus,inc', 'latitude': 8.4855, 'longitude': 76.9492, 'org': 'Vodafone India Ltd.', 'postal': '695021', 'region': 'Kerala', 'region_code': 'KL', 'timezone': 'Asia/Kolkata', 'utc_offset': '+0530', 'version': 'IPv4'}}]
    # refs = {
    #     "https://athul.github.io/notes/all.html": 6,
    #     "https://athul.github.io/notes/posts/git-tags.html": 1,
    #     "https://athul.github.io/notes/posts/air-zettel.html": 1,
    #     "https://athul.github.io/notes/": 1,
    #     "https://athul.github.io/notes/posts/golang.html": 1,
    #     "https://athul.github.io/notes/posts/git-cherry.html": 1,
    # }
    # hiturls = {
    #     "athul.github.io/notes/posts/air-zettel.html": 4,
    #     "athul.github.io/notes/posts/toc.html": 3,
    #     "athul.github.io/notes/all.html": 2,
    #     "athul.github.io/notes/posts/golang.html": 1,
    #     "athul.github.io/notes/": 1,
    #     "athul.github.io/notes/posts/git-tags.html": 1,
    # }
    # hours = ["14", "17", "20", "13"]
    # hhits = [3, 7, 1, 1]
    # days = [
    #     "2020/11/06",
    #     "2020/11/07",
    #     "2020/11/08",
    #     "2020/11/09",
    #     "2020/11/10",
    #     "2020/11/11",
    #     "2020/11/12",
    # ]
    # hits = [3, 5, 11, 0, 24, 0, 12]
    # os = {"Mac OS X": 12, "Linux": 0, "Windows": 0, "Other": 0, "Android": 6, "iOS": 4}
    # dev = {"Desktop": 12, "Mobile": 10, "Other": 0}
    return templates.TemplateResponse("index.html",{
            "request":request,
            "title":TITLE,
            "refs":refs,
            "urls":hiturls,
            "dev":dev,
            "os":os,
            "cflg":ipSorted,
            "time ": ipSorted,
            "chart":js.render(
                hitarr=hits, days=days, hours=hours, hhits=hhits, dev=dev, os=os
            ),
        },
    )

    # return nw

