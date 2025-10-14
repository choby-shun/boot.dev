from hoopla.lib.word_normalizer import WordNormalizer


class InvertedIndex:
    def __init__(self):
        # token to the doc_ids map
        self.index = {}

        # doc_id to the tokens map
        self.docmap = {}

        self.normalizer = WordNormalizer()

    def __add_document(self, doc_id, text):
        tokens = self.normalizer.default_normalization(text)
        for token in tokens:
            self.index.set_default(token, []).append(doc_id)

        self.docmap[doc_id] = tokens
