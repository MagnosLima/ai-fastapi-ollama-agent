from pydantic import BaseSettings

class Settings(BaseSettings):
    llm_model: str = "qwen3:4b"
    llm_endpoint: str = "http://localhost:11434"

    class Config:
        env_file = ".env"
