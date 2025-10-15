import json
from abc import ABC, abstractmethod

MOVIE_PATH = "./data/movies.json"
STOP_WORDS_PATH = "./data/stopwords.txt"


class DataLoader(ABC):
    @abstractmethod
    def load(self):
        pass


class MovieDataLoader:
    def __init__(self, path=MOVIE_PATH):
        self.path = path

    def load(self) -> list:
        with open(self.path) as f:
            return json.load(f)["movies"]


class StopwordsDataLoader:
    def __init__(self, path=STOP_WORDS_PATH):
        self.path = path

    def load(self) -> list:
        with open(self.path) as f:
            return f.read().splitlines()
