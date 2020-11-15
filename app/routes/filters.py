import flag
import datetime


def flagize(value):
    try:
        return flag.flag(value)
    except:
        return ""


def hmantime(value):
    dtime = datetime.datetime.strptime(value, '%Y-%m-%d %H:%M:%S.%f%z')
    return dtime.strftime("%B %d %Y | %H:%M:%S")
