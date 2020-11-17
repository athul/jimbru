import flag
import datetime


def flagize(value):
    try:
        return flag.flag(value)
    except:
        return ""


def hmantime(value,sm:bool=False):
    print(value)
    dtime = datetime.datetime.strptime(value, '%Y-%m-%d %H:%M:%S.%f%z')
    if sm:
        return dtime.strftime("%I:%M %p")
    else:
        return dtime.strftime("%B %d %Y | %I:%M:%S %p")

def getConutryCode(value):
    cn = value.split("|")
    return f"{flag.flag(cn[0])}  {cn[1]}"