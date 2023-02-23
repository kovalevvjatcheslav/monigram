from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    HEC_TOKEN: str = Field(..., env="HEC_TOKEN")
    TELEGRAM_APP_ID: int = Field(..., env="TELEGRAM_APP_ID")
    TELEGRAM_APP_HASH: str = Field(..., env="TELEGRAM_APP_HASH")
    TELEGRAM_BOT_TOKEN: str = Field(..., env="TELEGRAM_BOT_TOKEN")
    CHAT_ID: str = Field(..., env="CHAT_ID")
    HEC_SPLUNK_URL: str = Field("http://localhost:8088/services/collector", env="HEC_SPLUNK_URL")
    LOGGING_LEVEL: str = Field("INFO", env="LOGGING_LEVEL")


settings = Settings()
