import flag
import datetime


def flagize(value):
    try:
        return flag.flag(value)
    except:
        return ""


def hmantime(value):
    print(value)
    dtime = datetime.datetime.strptime(value, '%Y-%m-%d %H:%M:%S.%f%z')
    return dtime.strftime("%B %d %Y | %H:%M:%S")

def getConutryCode(value):
    cn = value.split("|")
    return f"{flag.flag(cn[0])}  {cn[1]}"