from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str
    DOCKER_SHM_SIZE: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    def __init__(self, **data):
        super().__init__(**data)
