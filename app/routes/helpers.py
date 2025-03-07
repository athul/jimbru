from typing import Dict, Tuple
from fastapi import Request
from datetime import datetime, timedelta
from pytz import timezone
from collections import Counter
from .model import db, Pageviews, URL
from os import path
import requests
from user_agents import parse


pth = path.dirname(__file__)


def getDatafromIP(ip):
    data = requests.get(f"https://ipapi.co/{ip}/json/").json()
    return data


def getDeviceDetails(agent) -> str:
    ua = parse(agent)
    device_type = "Other 👽"
    browser = ua.browser.family or ""
    os = ua.os.family
    device = ua.device.family or ua.device.model or ""
    if (
        ua.is_bot
        or (ua.browser.family or "").strip().lower() == "googlebot"
        or (ua.device.family or ua.device.model or "").strip().lower()
        == "spider"
    ):
        device_type = "Robot 🤖"
    elif ua.is_mobile:
        device_type = "Phone 📱"
    elif ua.is_tablet:
        device_type = "Tablet ⬆️📱"
    elif ua.is_pc:
        device_type = "Desktop 🖥"
    return browser, device_type, device, os



def pushtoDB(req: Request) -> Dict:
    """
    @args: Request class
    """
    url = URL(url=req.query_params["url"])
    now = datetime.now().astimezone(timezone("Asia/Kolkata"))
    referrer = req.query_params["ref"] or ""
    loadTime = req.query_params["lt"] or ""
    headers = dict(req.headers)
    bro, dev_type, dev, os = getDeviceDetails(headers['user-agent'])
    ipdata = getDatafromIP(headers["x-real-ip"])
    ipdata['model'] = dev
    ipdata['os'] = os
    ipdata['browser'] = bro
    
    data = Pageviews(
        url=f"{url.url.scheme}://{url.url.host}{url.url.path}",
        referrer=referrer,
        headers=headers,
        day=now.strftime("%Y/%m/%d"),
        time=str(now),
        ip=ipdata,
        ip_addr=headers["x-real-ip"] or "",
        hour=now.strftime("%H"),
        device_browser=bro,
        device=dev,
        device_type=dev_type,
        loadtime=loadTime,
        os=os,
    )
    if any(l in url.url.host for l in ["localhost", "127.0.0.1"]):
        return {"msg": "no-data pushed"}
    else:
        db.put(vars(data))
        return vars(data)

def getAllthings(ip:bool=False,dayNeed:bool=False):
    data = next(db.fetch())
    refs = []
    urls = []
    hours = []
    iptime = []
    dev = []
    devtype = []
    browser = []
    loadTime = []
    countries = []
    urlfromIP = []
    days = {}    
    today = datetime.now().astimezone(timezone("Asia/Kolkata"))
    for datum in data:
        refs.append(datum["referrer"])
        urls.append(datum["url"])
        hours.append(datum["hour"])
        iptime.append({datum["time"]: datum["ip"]})
        dev.append(datum['os'])
        browser.append(datum['device_browser'])
        devtype.append(datum['device_type'])
        loadTime.append(int(datum['loadtime']))
        countries.append(f'{datum["ip"]["country"]}|{datum["ip"]["country_name"]}')
        urlfromIP.append({datum['ip_addr']:{"time":datum['time'],"url":datum['url'],"ref":datum['referrer'],"ldt":datum['loadtime']}})
       
    for i in range(0, 30):
        day = (today - timedelta(days=i)).strftime("%Y/%m/%d")
        days[day]=0
        for d in data:
            if d.get('day') == day:
                days[day]+=1
    sortedDays = {k:v for k,v in sorted(days.items(), key=lambda item: item[0])}
    if dayNeed:
        return sortedDays
    if ip:
        return iptime,urlfromIP
    
    refListCleaned = list(Counter(refs).keys())
    for i in range(len(refListCleaned)):
        if refListCleaned[i] == "":
            refListCleaned[i] = "Direct"
    refListNos = list(Counter(refs).values())
    # ---
    urlListCleaned = list(Counter(urls).keys())
    urlHitNos = list(Counter(urls).values())
    # ---
    HourListCleaned = list(Counter(hours).keys())
    HourHitNos = list(Counter(hours).values())
    # ---
    countryCleaned = list(Counter(countries).keys())
    CountryNos = list(Counter(countries).values())
    # ---
    deviceList = list(Counter(dev).keys())
    deviceListNos = list(Counter(dev).values())
    # ---
    browserListCl = list(Counter(browser).keys())
    browserListNos = list(Counter(browser).values())
    # ---
    devtypeList = list(Counter(devtype).keys())
    devtypeNos = list(Counter(devtype).values())
    # ---
    browserDict = {browserListCl[i]: browserListNos[i]
                   for i in range(len(browserListCl))}
    deviceDict = {deviceList[i]: deviceListNos[i]
                  for i in range(len(deviceList))}
    refDict = {refListCleaned[i]: refListNos[i]
               for i in range(len(refListCleaned))}
    urlHitDict = {urlListCleaned[i]: urlHitNos[i]
                  for i in range(len(urlListCleaned))}
    devtypeDict = {devtypeList[i]: devtypeNos[i]
                   for i in range(len(devtypeList))}
    countryDict = {countryCleaned[i]:CountryNos[i] for i in range(len(countryCleaned))}
    # ---
    browserSortDict = {
        k: v for k, v in sorted(browserDict.items(), key=lambda item: item[1], reverse=True)
    }
    devtypeSortDict ={
        k: v for k, v in sorted(devtypeDict.items(), key=lambda item: item[1], reverse=True)
    }
    refSortDict = {
        k: v for k, v in sorted(refDict.items(), key=lambda item: item[1], reverse=True)
    }
    deviceSortDict = {
        k: v for k, v in sorted(deviceDict.items(), key=lambda item: item[1], reverse=True)
    }
    urlHitSortDict = {
        k: v
        for k, v in sorted(urlHitDict.items(), key=lambda item: item[1], reverse=True)
    }
    avgLoadTime = (sum(loadTime)/len(loadTime))
    
    return refSortDict, urlHitSortDict, HourListCleaned, HourHitNos, iptime, sum(urlHitNos), deviceSortDict, browserSortDict,devtypeSortDict,avgLoadTime,countryDict
