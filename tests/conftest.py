import pytest


@pytest.fixture
def minimal_weather_api_response():
    return {
        "latitude": 35.7,
        "longitude": 139.6875,
        "timezone": "GMT",
        "elevation": 40.0,
        "hourly_units": {
            "temperature_2m": "°C",
            "windspeed_10m": "km/h",
        },
        "hourly": {
            "time": [0, 3600],
            "temperature_2m": [20.0, 21.5],
            "windspeed_10m": [10.0, 12.0],
        },
    }
