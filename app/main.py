from fastapi import FastAPI
try:
    from routes import analytics,templates,auth
except:
    from .routes import analytics,templates,auth


app = FastAPI()

app.include_router(analytics.router)
app.include_router(templates.router)
app.include_router(auth.authr)