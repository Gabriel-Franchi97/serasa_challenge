# serasa_challenge

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-gree.svg)](https://www.python.org/)
[![Generic badge](https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white)](https://fastapi.tiangolo.com/)

### CRUD Application for taxi fare data for ML Prediction

# <a name="Deps"></a>Dependencies

This project is built with:

* Python (3.10)
* Poetry
* FastAPI
* [SqlAlchemy](http://sqlalchemy.org/)
* Docker
* Postgres
* Pytest (for testing)

For complete dependencies and details on some tools configurations see [pyproject.toml](pyproject.toml)

# <a name="Setup"></a>Setup
This project is using Docker, so you do not need to configure it locally, just make sure Docker is installed on your machine. Follow these steps:

```shell
docker-compose build

# To run the application
docker-compose up -d app
```

# <a name="Application-Structure"></a> Application Structure

```
.
├── .dockerignore
├── .env
├── .github
├── Dockerfile
├── Dockerfile.dev
├── README.md
├── alembic.ini
├── docker-compose.yml
├── serasa_challenge
│   ├── __init__.py
│   ├── api
│   ├── configs.py
│   ├── commands
│   ├── exceptions.py
│   ├── db
│   ├── main.py
├── poetry.lock
├── pyproject.toml
├── scripts
│   ├── start-lint.sh
│   ├── start.sh
├── setup.cfg
└── tests
    ├── __init__.py
    ├── conftest.py
    ├── api
    ├── commands
    └── test.parquet
```

# <a name="Database"></a>Database and migrations

For database migrations this project uses [Alembic](https://alembic.sqlalchemy.org/en/latest/).

The main commands:

## Generate a new migration/revision

`alembic revision -m "Migration descriptive message" --autogenerate`


## Apply the latest revision
`alembic upgrade head`

## To insert data from parquet files

Add the parquet file in the project structure and run the following commands:

`docker-compose exec app bash` To enter the container.

`export PYTHONPATH=/app:$PYTHONPATH` Setting the PYTHONPATH env variable to add the project's root directory 
to the Python module search path.

`python serasa_challenge/commands/bulk_create_taxi_fares.py {parquet file path}`
