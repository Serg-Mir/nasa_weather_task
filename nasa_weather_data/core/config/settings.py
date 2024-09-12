from functools import lru_cache

from pydantic_settings import BaseSettings
from pydantic import HttpUrl


class Settings(BaseSettings):
    debug: bool = False
    regional_api_url: HttpUrl = "https://power.larc.nasa.gov/api/temporal/monthly/regional"
    point_api_url: HttpUrl = "https://power.larc.nasa.gov/api/temporal/monthly/point"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache(maxsize=1)
def get_settings():
    return Settings()
