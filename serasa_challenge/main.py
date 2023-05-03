from fastapi import Depends
from fastapi import FastAPI

from serasa_challenge.api.v1.router import router
from serasa_challenge.configs import settings
from serasa_challenge.db.deps import get_db


def get_app() -> FastAPI:
    _app = FastAPI(
        title=settings.PROJECT_NAME,
        debug=settings.DEBUG,
        dependencies=[Depends(get_db)],
    )

    _app.include_router(router=router, prefix="/api")

    return _app


app = get_app()
