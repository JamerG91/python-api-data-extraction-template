from client import fetch_data
from config import (
    BASE_URL,
    HEADERS,
    PARAMS,
    EXPORT_FORMAT,
    OUTPUT_PATH,
    INPUT_PATH,
    SKIP_PARSING,
    USE_LOCAL_INPUT,
    CITY_COORDINATES,
)
from loaders.json_loader import JSONLoader
from loaders.csv_loader import CSVLoader
from loaders.excel_loader import ExcelLoader
from exporters.json_exporter import JSONExporter
from exporters.csv_exporter import CSVExporter
from exporters.excel_exporter import ExcelExporter
from parsers.weather_hourly_parser import WeatherHourlyParser


def get_loader(input_path):
    if input_path.endswith(".json"):
        return JSONLoader(input_path)
    if input_path.endswith(".csv"):
        return CSVLoader(input_path)
    if input_path.endswith((".xlsx", ".xls")):
        return ExcelLoader(input_path)
    raise ValueError("Unsupported input format")


def get_exporter(export_format, output_path):
    if export_format == "json":
        return JSONExporter(output_path)
    if export_format == "csv":
        return CSVExporter(output_path)
    if export_format == "excel":
        return ExcelExporter(output_path)
    raise ValueError("Unsupported export format")


def main():

    if not USE_LOCAL_INPUT:
        print("API data extraction template")
        all_raw_data = {}
        for city, (lat, lon) in CITY_COORDINATES.items():
            print(f"Fetching data for {city} (lat: {lat}, lon: {lon})")
            PARAMS["latitude"] = str(lat)
            PARAMS["longitude"] = str(lon)

            raw_data = fetch_data(url=BASE_URL, params=PARAMS, headers=HEADERS)
            all_raw_data[city] = raw_data
            print(f"Fetched data type: {type(raw_data).__name__}")
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

    exporter = get_exporter(EXPORT_FORMAT, OUTPUT_PATH)
    exporter.export_multiple_sheets(parsed_data)
    print(f"Data exported to {OUTPUT_PATH} in {EXPORT_FORMAT} format.")


if __name__ == "__main__":
    main()
