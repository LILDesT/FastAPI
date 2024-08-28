from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# Import the settings instance from config
from FastAPI.config import settings

# Create an asynchronous engine using the DATABASE_URL from settings
engine = create_async_engine(settings.DATABASE_URL, echo=True)

# Create an asynchronous session maker
async_session_maker = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Create a base class for declarative class definitions
Base = declarative_base()