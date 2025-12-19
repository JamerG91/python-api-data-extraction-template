# exporters/csv_exporter.py
import csv
from .base import Exporter


class CSVExporter(Exporter):
    def __init__(self, output_path: str):
        self.output_path = output_path

    def export(self, data):
        if not data:
            return

        # assumes list of dicts
        fieldnames = data[0].keys()

        with open(self.output_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
