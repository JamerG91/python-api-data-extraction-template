# loaders/json_loader.py
import json
from .base import Loader


class JSONLoader(Loader):
    def __init__(self, path: str):
        self.path = path

    def load(self):
        with open(self.path, "r", encoding="utf-8") as f:
            return json.load(f)
