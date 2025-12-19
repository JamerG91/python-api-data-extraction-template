# Request Configuration
USE_API = True
BASE_URL = "https://api.open-meteo.com/v1/forecast"
TIMEOUT = 10
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/143.0.0.0 Safari/537.36"
    )
}

# Input/Output Configuration
INPUT_PATH = r"data\meteo.json"  # or "data\local_data.csv"

OUTPUT_PATH = r"output\meteo_ouput.csv"  # or "output.csv"

# use to export raw data without parsing
SKIP_PARSING = False


HOURLY_PARAMS = [
    "temperature_2m",
    "relative_humidity_2m",
    "apparent_temperature",
    "precipitation",
    "weathercode",
    "windspeed_10m",
]

PARAMS = {
    "latitude": "35.6895",
    "longitude": "139.6917",
    "hourly": ",".join(HOURLY_PARAMS),
    "format": "json",
    "timeformat": "unixtime",
}

CITY_COORDINATES = {
    "Tokyo": (35.6895, 139.6917),
    "New York": (40.7128, -74.0060),
    "London": (51.5074, -0.1278),
    "Sydney": (-33.8688, 151.2093),
    "Mumbai": (19.0760, 72.8777),
    "Cairo": (30.0444, 31.2357),
    "Rio de Janeiro": (-22.9068, -43.1729),
    "Paris": (48.8566, 2.3522),
    "Moscow": (55.7558, 37.6173),
    "Toronto": (43.651070, -79.347015),
    "Beijing": (39.9042, 116.4074),
    "Berlin": (52.5200, 13.4050),
    "Madrid": (40.4168, -3.7038),
    "Rome": (41.9028, 12.4964),
    "Bangkok": (13.7563, 100.5018)
}

