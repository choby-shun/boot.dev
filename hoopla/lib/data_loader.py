import json
from abc import ABC, abstractmethod


class DataLoader(ABC):
    @abstractmethod
    def load(self):
        pass


class MovieDataLoader:
    def __init__(self, path):
        self.path = path

    def load(self) -> list:
        with open(self.path) as f:
            return json.load(f)["movies"]


class StopwordsDataLoader:
    def __init__(self, path):
        self.path = path

    def load(self) -> list:
        with open(self.path) as f:
            return f.read().splitlines()
