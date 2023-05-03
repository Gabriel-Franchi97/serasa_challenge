import pytest

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy_utils import create_database
from sqlalchemy_utils import database_exists
from sqlalchemy_utils import drop_database

from serasa_challenge.configs import settings
from serasa_challenge.db import models
from serasa_challenge.db import schemas
from serasa_challenge.db.base import Base
from serasa_challenge.db.deps import get_db
from serasa_challenge.main import app


@pytest.fixture(scope="session")
def db_engine():
    TEST_DB_NAME = f"{settings.DB_URI}_test"

    engine = create_engine(TEST_DB_NAME)
    if not database_exists(engine.url):
        create_database(engine.url)

    Base.metadata.create_all(bind=engine)
    yield engine

    drop_database(TEST_DB_NAME)


@pytest.fixture(scope="function")
def db(db_engine):
    connection = db_engine.connect()

    # begin a non-ORM transaction
    connection.begin()

    # bind an individual Session to the connection
    db = Session(bind=connection)

    yield db

    db.rollback()
    connection.close()


@pytest.fixture(scope="function")
def app_client(db):
    app.dependency_overrides[get_db] = lambda: db

    with TestClient(app) as c:
        yield c


@pytest.fixture
def taxi_fare(db):
    data = {
        "key": "2023-04-27T19:11:34.350Z",
        "fare_amount": "0",
        "pickup_datetime": "2023-04-27T19:11:34.350Z",
        "pickup_longitude": "-74.010482788085938",
        "pickup_latitude": "0.717666625976562",
        "dropoff_longitude": "-73.985771179199219",
        "dropoff_latitude": "0.660366058349609",
        "passenger_count": "1",
    }
    taxi_fare = schemas.TaxiFareCreate(**data)
    instance = models.TaxiFare(**taxi_fare.dict())
    instance.save(db)

    return instance
