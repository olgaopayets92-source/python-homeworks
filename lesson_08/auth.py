import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("YOUGILE_API_KEY")


def get_token():
    if not API_KEY:
        raise ValueError("YOUGILE_API_KEY не установлен в .env")
    return API_KEY
