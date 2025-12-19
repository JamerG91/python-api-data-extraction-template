from datetime import datetime, timezone
from parsers.base import Parser


UNIT_SUFFIX_MAP = {
    "°C": "c",
    "%": "pct",
    "mm": "mm",
    "km/h": "kmh",
    "wmo code": "wmo",
}


def unix_to_iso(timestamp: int) -> str:
    return datetime.fromtimestamp(
        timestamp,
        tz=timezone.utc,
    ).isoformat()


class WeatherHourlyParser(Parser):
    def parse(self, data: dict) -> list[dict]:
        hourly = data.get("hourly", {})
        units = data.get("hourly_units", {})
        times = hourly.get("time", [])

        if not times:
            return []

        # Metadata shared across all rows
        metadata = {
            "latitude": data.get("latitude"),
            "longitude": data.get("longitude"),
            "timezone": data.get("timezone"),
            "elevation": data.get("elevation"),
        }

        parsed_rows = []

        for idx, ts in enumerate(times):
            row = {
                "time_iso": unix_to_iso(ts),
                **metadata,
            }

            for key, values in hourly.items():
                if key == "time":
                    continue

                unit = units.get(key)
                suffix = UNIT_SUFFIX_MAP.get(unit, "value")
                column_name = f"{key}_{suffix}"

                row[column_name] = values[idx] if idx < len(values) else None

            parsed_rows.append(row)

        return parsed_rows
