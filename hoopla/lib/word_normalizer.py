import string

from nltk.stem import PorterStemmer

from hoopla.lib.data_loader import StopwordsDataLoader

STOP_WORDS_PATH = "./data/stopwords.txt"


class WordNormalizer:
    def __init__(self, stop_word_fp: str = STOP_WORDS_PATH, stemmer=PorterStemmer()):
        self.chain = []
        self.stemmer = stemmer
        self.stop_words = StopwordsDataLoader(stop_word_fp).load()

    def remove_punc(self):
        def _remove_punc(text):
            return text.translate(str.maketrans("", "", string.punctuation))

        self.chain.append(_remove_punc)
        return self

    def lower_string(self):
        def _lower_string(text):
            return text.lower()

        self.chain.append(_lower_string)
        return self

    def tokenization(self):
        def _tokenization(text):
            return text.split()

        self.chain.append(_tokenization)
        return self

    def remove_stop_words(self):
        def _remove_stop_words(text):
            return [text for text in text if text not in self.stop_words]

        self.chain.append(_remove_stop_words)
        return self

    def stem(self):
        def _stem(text):
            return [self.stemmer.stem(text) for text in text]

        self.chain.append(_stem)
        return self

    def start(self):
        self.chain = []
        return self

    def run(self, text):
        for func in self.chain:
            text = func(text)
        return text

    def default_normalization(self, text):
        return (
            self.start()
            .remove_punc()
            .lower_string()
            .tokenization()
            .remove_stop_words()
            .stem()
            .run(text)
        )
