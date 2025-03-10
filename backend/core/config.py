from pathlib import Path
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent  # full path to the current file


class Setting(BaseSettings):
    api_v1_prefix: str = '/api/v1'
    db_url: str = f'sqlite+aiosqlite:///{BASE_DIR}/db.sqlite3'  # file path
    db_echo: bool = True  # debug mode


settings = Setting()
