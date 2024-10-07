from pydantic import BaseModel
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()


class BdSetting(BaseModel):
    url: str
    echo: bool = True


class Setting(BaseSettings):
    db: BdSetting = BdSetting(url=os.getenv('DATABASE_URL'))


setting = Setting()