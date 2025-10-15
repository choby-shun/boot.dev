from hoopla.lib.inverted_index import InvertedIndex


def keyword_search(index, query: str):
    docs = index.get_documents(query)
    return docs
