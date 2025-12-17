# Configuration placeholders
BASE_URL = "https://api.open-meteo.com/v1/forecast"
TIMEOUT = 10
HEADERS = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36" }
PARAMS = {
    "latitude": "35.6895",
    "longitude": "139.6917",
    "hourly": "temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,weathercode,windspeed_10m",
    "format": "json",
    "timeformat": "unixtime"}