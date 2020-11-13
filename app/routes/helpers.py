from typing import Dict,Tuple
from fastapi import Request
from datetime import datetime,timedelta
from pytz import timezone
from collections import Counter
from .model import db,Pageviews,URL
from os import path
import requests

pth = path.dirname(__file__)

def getDatafromIP(ip):
    data = requests.get(f"https://ipapi.co/{ip}/json/").json()
    return data

def getHitsPerDay():
    """
    return 2 lists
    """
    today = datetime.now().astimezone(timezone('Asia/Kolkata'))
    hits = []
    days = []
    for i in range(0, 7):
        day = (today - timedelta(days=i)).strftime("%Y/%m/%d")
        days.append(day)
        day_hits = db.fetch({"day": day})
        hits.append(len(next(day_hits)))
    return days[::-1], hits[::-1]

def pushtoDB(req: Request) -> Dict:
    """ 
    @args: Request class
    """
    url = URL(url=req.query_params["url"])
    # if "localhost" or "127.0.0.1" in url.url.host:
    #     return {"msg": "no-data pushed"}
    now = datetime.now().astimezone(timezone('Asia/Kolkata'))
    print("Host",req.client.host)
    referrer = req.query_params["ref"] or ""
    headers = dict(req.headers)
    print(req['headers'])
    ipdata = getDatafromIP(headers['x-real-ip'])
    data = Pageviews(
        url=f"{url.url.host}{url.url.path}",
        referrer=referrer,
        headers=headers,
        day=now.strftime("%Y/%m/%d"),
        time=str(now),
        ip=ipdata,
        hour=now.strftime("%H"),
    )
    print(now.strftime("%B %d, %Y %H:%M:%S"))
    db.put(vars(data))
    return vars(data)

def getAllthings():
    data = next(db.fetch())
    refs = []
    urls = []
    hours = []
    devices = []
    iptime = []
    android=mac=win=linux=other=phone=desktop=ios=oth_os = 0
    for datum in data:
        refs.append(datum["referrer"])
        urls.append(datum["url"])
        hours.append(datum["hour"])
        devices.append(datum['headers']['user-agent'].strip())
        iptime.append({"time":datum['time'],"ip":datum['ip']})
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
    return refSortDict, urlHitSortDict, HourListCleaned, HourHitNos,OS,DEVICES,iptime


