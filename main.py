from client import fetch_data
from config import (
    USE_API,
    BASE_URL,
    HEADERS,
    PARAMS,
    OUTPUT_PATH,
    INPUT_PATH,
    SKIP_PARSING,
    CITY_COORDINATES,
    USE_CACHE,
)
from loaders.json_loader import JSONLoader
from loaders.csv_loader import CSVLoader
from loaders.excel_loader import ExcelLoader
from exporters.json_exporter import JSONExporter
from exporters.csv_exporter import CSVExporter
from exporters.excel_exporter import ExcelExporter
from parsers.parser import WeatherHourlyParser

from pathlib import Path
import json
from datetime import datetime


def get_loader(input_path):
    if input_path.endswith(".json"):
        return JSONLoader(input_path)
    if input_path.endswith(".csv"):
        return CSVLoader(input_path)
    if input_path.endswith((".xlsx", ".xls")):
        return ExcelLoader(input_path)
    raise ValueError("Unsupported input format")


def get_exporter(output_path):
    if "json" in output_path:
        return JSONExporter(output_path)
    elif "csv" in output_path:
        return CSVExporter(output_path)
    elif "xlsx" in output_path or "xls" in output_path:
        return ExcelExporter(output_path)
    else:
        raise ValueError("Unsupported export format")


def main():

    # import json exporter for caching purposes
    CACHE_PATH = r"data\cache.json"
    cache_exporter = JSONExporter(CACHE_PATH)

    cache = {
        "completed": {},
        "failed": {},
        "meta": {
            "requests_made": 0,
            "started_at": datetime.utcnow().isoformat() + "Z",
            "api_url": BASE_URL,
        },
    }

    if Path(CACHE_PATH).exists() and USE_CACHE:
        with open(CACHE_PATH, encoding="utf-8") as f:
            cache = json.load(f)

    if USE_API:
        print("API data extraction template")

        # create a copy of PARAMS to avoid mutating the original
        params = PARAMS.copy()
        for city, (lat, lon) in CITY_COORDINATES.items():
            if city in cache["completed"]:
                print(f"Skipping {city}, already cached")
                continue

            print(f"Fetching data for {city} (lat: {lat}, lon: {lon})")
            params["latitude"] = str(lat)
            params["longitude"] = str(lon)

            raw_data = fetch_data(url=BASE_URL, params=params, headers=HEADERS)
            print(
                f"Fetch result for {city}: " f"{'OK' if raw_data['ok'] else 'FAILED'}"
            )

            if raw_data["ok"]:
                cache["completed"][city] = raw_data["data"]
            else:
                cache["failed"][city] = raw_data["error"]

            cache["meta"]["requests_made"] += 1

            if cache["meta"]["requests_made"] % 30 == 0:
                cache_exporter.export(cache)

        all_raw_data = cache["completed"]
        cache_exporter.export(cache)

    else:
        print("Local file data extraction template")
        if not INPUT_PATH:
            raise ValueError("USE_LOCAL_INPUT is True but INPUT_PATH is not set.")
        loader = get_loader(INPUT_PATH)
        all_raw_data = {"local_data": loader.load()}

    if not SKIP_PARSING:
        parsed_data = {}
        parser = WeatherHourlyParser()
        for city, raw_data in all_raw_data.items():
            print(f"Parsing data for {city}")
            city_parsed_data = parser.parse(raw_data)
            parsed_data[city] = city_parsed_data
    else:
        parsed_data = all_raw_data

    exporter = get_exporter(OUTPUT_PATH)
    exporter.export(parsed_data)
    print(f"Data exported to {OUTPUT_PATH} in {OUTPUT_PATH.split('.')[-1]} format.")


if __name__ == "__main__":
    main()
