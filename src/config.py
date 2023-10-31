from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    TELEGRAM_ACCESS_TOKEN: str

    MONGODB_HOST: str
    MONGODB_PORT: int
    MONGODB_DATABASE: str
    MONGODB_USERNAME: str
    MONGODB_PASSWORD: str


settings = Settings()
