import os
from dotenv import load_dotenv
load_dotenv()

title = os.getenv("TITLE")
SECRET = os.getenv("SECRET_JWT")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
deta_key = os.getenv("PKEY")
deta_pname = os.getenv("PNAME")
domain = os.getenv("DOMAIN")
