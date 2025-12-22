import csv
from .base import Exporter
from pathlib import Path


class CSVExporter(Exporter):
    def __init__(self, output_path: str):
        self.output_path = Path(output_path)

    def export(self, data):
        """
        Export data to CSV.

        - If data is a list of dicts → single CSV file
        - If data is a dict[str, list[dict]] → one CSV per key
        """
        if not data:
            return

        if isinstance(data, list):
            self._export_single(self.output_path, data)
        elif isinstance(data, dict):
            self._export_multiple(data)
        else:
            raise TypeError(
                "CSVExporter expects a list[dict] or dict[str, list[dict]]"
            )

    def _export_single(self, path: Path, rows: list[dict]):
        if not rows:
            return

        fieldnames = rows[0].keys()

        with path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    def _export_multiple(self, datasets: dict[str, list[dict]]):
        base = self.output_path.with_suffix("")

        for name, rows in datasets.items():
            if not rows:
                continue

            safe_name = name.replace(" ", "_")
            path = base.parent / f"{safe_name}.csv"
            self._export_single(path, rows)
