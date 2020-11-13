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
    return dtime.strftime("%d %B %Y | %H:%M:%S")
