# loaders/csv_loader.py
import csv
from .base import Loader


class CSVLoader(Loader):
    def __init__(self, path: str):
        self.path = path

    def load(self):
        with open(self.path, newline="", encoding="utf-8") as f:
            return list(csv.DictReader(f))
