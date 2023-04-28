from fastapi import APIRouter

from serasa_challenge.api.v1.endpoints.taxi_fare import router as rt

router = APIRouter(prefix="/v1")
router.include_router(rt.router)
