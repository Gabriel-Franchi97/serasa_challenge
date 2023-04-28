import argparse

import pandas as pd

from sqlalchemy.orm import Session

from serasa_challenge.db.deps import get_db
from serasa_challenge.db.models import TaxiFare


def bulk_create_taxi_fares(db: Session, taxi_fares: pd.DataFrame):
    """Bulk creates TaxiFare records in the database."""
    records = []
    for _, row in taxi_fares.iterrows():
        record = TaxiFare(
            key=row["key"],
            fare_amount=row["fare_amount"] if "fare_amount" in row else None,
            pickup_datetime=row["pickup_datetime"],
            pickup_longitude=row["pickup_longitude"],
            pickup_latitude=row["pickup_latitude"],
            dropoff_longitude=row["dropoff_longitude"],
            dropoff_latitude=row["dropoff_latitude"],
            passenger_count=row["passenger_count"],
        )
        records.append(record)

    db.bulk_save_objects(records)
    db.commit()


if __name__ == "__main__":
    # Define command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=str, help="Path to the .parquet file")

    args = parser.parse_args()

    taxi_fares = pd.read_parquet(args.file)

    with get_db() as db:
        with db.begin():
            bulk_create_taxi_fares(db, taxi_fares)
