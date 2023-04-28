from typing import Any
from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi.params import Query
from sqlalchemy.orm import Session
from starlette import status

from serasa_challenge.db import models
from serasa_challenge.db import schemas
from serasa_challenge.db.deps import get_db

router = APIRouter()


@router.get("/taxi-fare/", response_model=List[schemas.TaxiFare])
def list_taxi_fares(
    limit: int = Query(100, gt=0, le=1000), offset: int = Query(0, ge=0), db: Session = Depends(get_db)  # type: ignore
) -> Any:
    instances = models.TaxiFare.list(limit=limit, offset=offset, db=db)
    return instances


@router.get("/taxi-fare/{taxi_fare_id}/", response_model=schemas.TaxiFare)
def get_taxi_fare(taxi_fare_id: int, db: Session = Depends(get_db)) -> Any:
    instance = models.TaxiFare.get_by_id(id=taxi_fare_id, db=db)
    if not instance:
        raise HTTPException(status_code=404, detail="Taxi Fare not found")
    return instance


@router.put("/taxi-fare/{taxi_fare_id}/", response_model=schemas.TaxiFare)
def update_taxi_fare(taxi_fare_id: int, data: schemas.TaxiFareCreate, db: Session = Depends(get_db)) -> Any:
    instance = models.TaxiFare.update(id=taxi_fare_id, update_data=data.dict(), db=db)
    if not instance:
        raise HTTPException(status_code=404, detail="Taxi Fare not found")
    return instance


@router.post("/taxi-fare/", response_model=schemas.TaxiFare, status_code=status.HTTP_201_CREATED)
def create_taxi_fare(data: schemas.TaxiFareCreate, db: Session = Depends(get_db)) -> Any:
    instance = models.TaxiFare(**data.dict())
    instance.save(db=db)
    return instance


@router.delete("/taxi-fare/{taxi_fare_id}/")
def delete_taxi_fare(taxi_fare_id: int, db: Session = Depends(get_db)) -> Any:
    deleted = models.TaxiFare.delete(id=taxi_fare_id, db=db)
    if not deleted:
        raise HTTPException(status_code=404, detail="Taxi Fare not found")
    return {"message": "Taxi Fare deleted successfully"}
