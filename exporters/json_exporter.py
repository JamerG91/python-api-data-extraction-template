import json
from .base import Exporter


class JSONExporter(Exporter):
    def __init__(self, output_path: str):
        self.output_path = output_path

    def export(self, data):
        with open(self.output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
