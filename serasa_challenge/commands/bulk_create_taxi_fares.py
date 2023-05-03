import argparse

import pandas as pd

from sqlalchemy import insert
from sqlalchemy.orm import Session

from serasa_challenge.db.deps import get_batch_db
from serasa_challenge.db.models import TaxiFare


def bulk_create_taxi_fares(db: Session, taxi_fares: pd.DataFrame):
    """Bulk creates TaxiFare records in the database."""
    records = taxi_fares.to_dict("records")
    stmt = insert(TaxiFare.__table__).values(records)
    db.execute(stmt)
    db.commit()


if __name__ == "__main__":
    # Define command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=str, help="Path to the .parquet file")

    args = parser.parse_args()

    taxi_fares = pd.read_parquet(args.file)

    with get_batch_db() as db:
        with db.begin():
            bulk_create_taxi_fares(db, taxi_fares)
