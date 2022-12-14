"""

database config settings

"""


from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from ...utils import get_env_var, load_env



load_env()



# database url
SQLALCHEMY_DATABASE_URL = get_env_var("DATABASE_URL")

ASYNC_SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://gwen@localhost/fast_lms"



# engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    future=True,
    echo=True
)

async_engine = create_async_engine(
    ASYNC_SQLALCHEMY_DATABASE_URL
)


# SessionLocal
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False, 
    bind=engine, 
    future=True
)

AsyncSessionLocal = sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)


# Base = declarative_base()


