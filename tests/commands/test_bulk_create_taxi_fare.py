import pandas as pd

from sqlalchemy.orm import Session

from serasa_challenge.commands.bulk_create_taxi_fares import bulk_create_taxi_fares
from serasa_challenge.db.models import TaxiFare


def test_bulk_create_taxi_fares(db: Session):
    taxi_fares = pd.DataFrame(
        {
            "key": ["2015-01-27T13:08:24Z", "2011-10-08T11:53:44Z"],
            "fare_amount": [10.0, 15.0],
            "pickup_datetime": ["2023-04-27T19:11:34.350Z", "2023-04-27T19:11:34.350Z"],
            "pickup_longitude": [-73.982683, -73.981],
            "pickup_latitude": [40.742975, 40.755],
            "dropoff_longitude": [-73.98345, -73.98],
            "dropoff_latitude": [40.762725, 40.76],
            "passenger_count": [1, 2],
        }
    )
    bulk_create_taxi_fares(db, taxi_fares)

    # Check that the records were created in the database
    assert db.query(TaxiFare).filter(TaxiFare.key.in_(["2015-01-27T13:08:24Z", "2011-10-08T11:53:44Z"])).count() == 2
