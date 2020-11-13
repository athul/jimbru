from fastapi import APIRouter,Request,Response
from base64 import b64decode
from .helpers import pushtoDB


router=APIRouter()

BEACON: str = b64decode("R0lGODlhAQABAIAAANvf7wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==")

DOMAIN: str = "https://smq654.deta.dev"
TITLE:str = "Notes Site"
JS: str = """(function(){
    var d=document,i=new Image,e=encodeURIComponent;
    i.src='%s/a.gif?url='+e(d.location.href)+'&ref='+e(d.referrer);
    })()""".replace("\n", "")

@router.get("/a.gif")
def getImg(request: Request):
    pushtoDB(request)
    return Response(
        content=BEACON,
        media_type="img/gif",
        headers={"Cache-Control": "private, no-cache"},
    )


@router.get("/a.js")
def getJs():
    return Response(content=JS % DOMAIN, media_type="text/javascript")