from starlette import status

from serasa_challenge.db.models import TaxiFare


class TestRouterTaxiFare:
    TAXI_FARE_URL = "/api/v1/taxi-fare/"

    def test_create_taxi_fare(self, app_client, db):
        payload = {
            "key": "2023-04-27T19:11:34.350Z",
            "fare_amount": "0",
            "pickup_datetime": "2023-04-27T19:11:34.350Z",
            "pickup_longitude": "-74.010482788085938",
            "pickup_latitude": "0.717666625976562",
            "dropoff_longitude": "-73.985771179199219",
            "dropoff_latitude": "0.660366058349609",
            "passenger_count": "1",
        }

        response = app_client.post(self.TAXI_FARE_URL, json=payload)
        id = response.json().get("id")

        assert response.status_code == status.HTTP_201_CREATED
        assert TaxiFare.get_by_id(id=id, db=db)

    def test_get_taxi_fare(self, app_client, taxi_fare):
        url = f"{self.TAXI_FARE_URL}{taxi_fare.id}"

        response = app_client.get(url)

        assert response.status_code == status.HTTP_200_OK

    def test_update_taxi_fare(self, app_client, db, taxi_fare):
        payload = {
            "key": "2023-04-27T19:11:34.350Z",
            "fare_amount": "45",
            "pickup_datetime": "2023-04-27T19:11:34.350Z",
            "pickup_longitude": "-74.010482788085938",
            "pickup_latitude": "0.717666625976562",
            "dropoff_longitude": "-73.985771179199219",
            "dropoff_latitude": "0.660366058349609",
            "passenger_count": 3,
        }
        url = f"{self.TAXI_FARE_URL}{taxi_fare.id}/"

        response = app_client.put(url, json=payload)
        id = response.json().get("id")

        assert response.status_code == status.HTTP_200_OK
        assert TaxiFare.get_by_id(id=id, db=db).passenger_count == payload["passenger_count"]

    def test_delete_taxi_fare(self, app_client, taxi_fare, db):
        url = f"{self.TAXI_FARE_URL}{taxi_fare.id}/"

        response = app_client.delete(url)

        assert response.status_code == status.HTTP_200_OK
        assert not TaxiFare.get_by_id(id=taxi_fare.id, db=db)
