from typing import List
from typing import Optional

import sqlalchemy as sa

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from serasa_challenge.db.base import Base


class TaxiFare(Base):
    __tablename__ = "taxi_fare"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    key = sa.Column(sa.TIMESTAMP(), nullable=False)
    fare_amount = sa.Column(sa.DECIMAL(precision=6, scale=2), nullable=True)
    pickup_datetime = sa.Column(sa.TIMESTAMP(), nullable=False)
    pickup_longitude = sa.Column(sa.DECIMAL(precision=18, scale=15), nullable=False)
    pickup_latitude = sa.Column(sa.DECIMAL(precision=18, scale=15), nullable=False)
    dropoff_longitude = sa.Column(sa.DECIMAL(precision=18, scale=15), nullable=False)
    dropoff_latitude = sa.Column(sa.DECIMAL(precision=18, scale=15), nullable=False)
    passenger_count = sa.Column(sa.INTEGER, nullable=False)

    @classmethod
    def get_by_id(cls, id: int, db: Session) -> Optional["TaxiFare"]:
        return db.query(cls).filter(cls.id == id).first()

    @classmethod
    def update(cls, id: int, update_data: dict, db: Session) -> Optional["TaxiFare"]:
        instance = db.query(cls).filter(cls.id == id).first()
        if instance:
            for key, value in update_data.items():
                setattr(instance, key, value)
            db.add(instance)
            db.commit()
            db.refresh(instance)
        return instance

    @classmethod
    def delete(cls, id: int, db: Session) -> bool:
        instance = db.query(cls).filter(cls.id == id).first()
        if instance:
            db.delete(instance)
            db.commit()
            return True
        return False

    @classmethod
    def list(cls, limit: int, offset: int, db: Session) -> Optional[List["TaxiFare"]]:
        instances = db.query(cls).limit(limit).offset(offset).all()
        return instances

    def save(self, db: Session, commit: bool = True) -> None:
        db.add(self)
        try:
            if commit:
                db.commit()
                db.refresh(self)
            else:
                db.flush()
        except IntegrityError as e:
            self._raise_validation_exception(e)
