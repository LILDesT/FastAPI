from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# Define the database connection string
from config import settings

# Create a complete database URL

# Create an asynchronous engine
engine = create_async_engine(settings.DATABASE_URL, echo=True)

# Create an asynchronous session maker
async_session_maker = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Create a base class for declarative class definitions
Base = declarative_base()