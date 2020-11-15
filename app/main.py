from fastapi import FastAPI
try:
    from routes import analytics,templates
except:
    from .routes import analytics,templates


app = FastAPI()

app.include_router(analytics.router)
app.include_router(templates.router)