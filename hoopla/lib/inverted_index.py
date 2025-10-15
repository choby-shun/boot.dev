import os
import pickle

from hoopla.lib.data_loader import MovieDataLoader
from hoopla.lib.word_normalizer import WordNormalizer


class InvertedIndex:
    def __init__(self):
        # token to the doc_ids map
        self.index = {}
        self.index_cache_fp = "cache/index.pkl"

        # doc_id to the tokens map
        self.docmap = {}
        self.docmap_cache_fp = "cache/docmap.pkl"

        self.normalizer = WordNormalizer()
        self.movie_data_loader = MovieDataLoader()

    def __add_document(self, doc_id, text):
        tokens = self.normalizer.default_normalization(text)
        for token in tokens:
            self.index.setdefault(token, []).append(doc_id)

        self.docmap[doc_id] = tokens

    def get_documents(self, term):
        docs = self.index.get(term)
        if not docs:
            return []
        return sorted(docs)

    def build(self):
        data_pool = self.movie_data_loader.load()
        for movie in data_pool:
            text = f"{movie['title']} {movie['description']}"
            self.__add_document(movie["id"], text)

    def save(self):
        # Ensure cache directory exists
        os.makedirs("cache", exist_ok=True)

        with open(self.index_cache_fp, "wb") as f:
            pickle.dump(self.index, f)

        with open(self.docmap_cache_fp, "wb") as f:
            pickle.dump(self.docmap, f)

    def load(self):
        if not os.path.exists(self.index_cache_fp):
            raise FileNotFoundError(f"Missing index cache file: {index_path}")
        if not os.path.exists(self.docmap_cache_fp):
            raise FileNotFoundError(f"Missing docmap cache file: {docmap_path}")

        # Load both pickle files
        with open(self.index_cache_fp, "rb") as f:
            self.index = pickle.load(f)
        with open(self.docmap_cache_fp, "rb") as f:
            self.docmap = pickle.load(f)
