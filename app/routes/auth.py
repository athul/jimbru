from fastapi import APIRouter,Depends,status
from fastapi.responses import RedirectResponse,HTMLResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login import LoginManager
from .settings import SECRET,USERNAME,PASSWORD
from fastapi_login.exceptions import InvalidCredentialsException

authr = APIRouter()

manager = LoginManager(SECRET,tokenUrl="/auth/login",use_cookie=True)
manager.cookie_name = "jimbru"

DB = {USERNAME:{"password":PASSWORD}}

@manager.user_loader
def load_user(username:str):
    user = DB.get(username)
    return user

@authr.post("/auth/login")
def login(data: OAuth2PasswordRequestForm = Depends()):
    username = data.username
    password = data.password
    user = load_user(username)
    if not user:
        raise InvalidCredentialsException
    elif password != user['password']:
        raise InvalidCredentialsException
    
    access_token = manager.create_access_token(
        data={"sub":username}
    )
    resp = RedirectResponse(url="/dash",status_code=status.HTTP_302_FOUND)
    manager.set_cookie(resp,access_token)
    return resp

@authr.get("/private")
def logged_in_users_only(_=Depends(manager)):
    return "You are logged In"

