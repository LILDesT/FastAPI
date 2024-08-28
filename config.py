from pydantic_settings import BaseSettings

class Setting(BaseSettings):
    DB_HOST: str = 'localhost'
    DB_PORT: int = 5432
    DB_USER: str = 'postgres'
    DB_PASS: str = 'postgres'
    DB_NAME: str = 'postgres'
    
    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    class Config:
        env_file = 'APP/.env'
        env_file_encoding = 'utf-8'

settings = Setting()


#print(settings.DATABASE_URL)