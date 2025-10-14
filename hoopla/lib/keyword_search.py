from hoopla.lib.word_normalizer import WordNormalizer


def match(keyword, title):
    for kw in set(keyword):
        for t in set(title):
            if kw in t:
                return True
    return False


def keyword_search(data, query: str):
    normalizer = WordNormalizer()

    query = normalizer.default_normalization(query)
    returns = []

    for row in data:
        title = normalizer.default_normalization(row["title"])
        if match(query, title):
            returns.append(row)

    return returns
