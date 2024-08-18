from pydantic_settings import BaseSettings

class Setting(BaseSettings):
    DB_HOST: str = 'localhost'  # Default value if not provided by environment
    DB_PORT: int = 5432         # Default value if not provided by environment
    DB_USER: str = 'postgres'   # Default value if not provided by environment
    DB_PASS: str = 'postgres'   # Default value if not provided by environment
    DB_NAME: str = 'postgres'   # Default value if not provided by environment
    
    @property
    def DATABASE_URL(self) -> str:
        """Construct the database URL based on the settings."""
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    class Config:
        env_file = 'APP/.env'  # Specify a dotenv file to load variables from
        env_file_encoding = 'utf-8'
        
settings = Setting()

print(settings.DATABASE_URL)