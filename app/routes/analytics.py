from fastapi import APIRouter, Request, Response
from base64 import b64decode
from .helpers import pushtoDB
from .settings import domain, title

router = APIRouter()

BEACON: str = b64decode(
    "R0lGODlhAQABAIAAANvf7wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==")

DOMAIN: str = domain
TITLE: str = title
JS: str = """(function () {
    window.addEventListener('load', () => {
        i = new Image;
        i.src = '%s/a.gif?url=' + encodeURIComponent(document.location.href) + '&ref=' + encodeURIComponent(document.referrer) + '&lt=' + encodeURIComponent(window.performance.timing.domContentLoadedEventEnd - window.performance.timing.navigationStart);
    })
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
