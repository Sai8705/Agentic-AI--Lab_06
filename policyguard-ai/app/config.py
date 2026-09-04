from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "PolicyGuard AI"
    host: str = "127.0.0.1"
    port: int = 8005

settings = Settings()
