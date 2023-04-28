import datetime
import decimal

from typing import Optional

from pydantic import BaseModel


class Base(BaseModel):
    class Config:
        orm_mode = True


class TaxiFareBase(Base):
    key: datetime.datetime
    fare_amount: Optional[decimal.Decimal]
    pickup_datetime: datetime.datetime
    pickup_longitude: decimal.Decimal
    pickup_latitude: decimal.Decimal
    dropoff_longitude: decimal.Decimal
    dropoff_latitude: decimal.Decimal
    passenger_count: int


class TaxiFareCreate(TaxiFareBase):
    pass


class TaxiFare(TaxiFareBase):
    id: int
