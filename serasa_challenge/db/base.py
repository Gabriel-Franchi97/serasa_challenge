from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from serasa_challenge.configs import settings

engine = create_engine(
    settings.DB_URI,
    echo=settings.DB_ECHO,
    pool_size=settings.DB_POOL_SIZE,
    max_overflow=settings.DB_MAX_OVERFLOW,
    future=True,
)
session = sessionmaker(bind=engine, future=True)
metadata = MetaData()
Base = declarative_base(metadata=metadata)
