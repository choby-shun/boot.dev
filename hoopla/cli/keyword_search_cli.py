#!/usr/bin/env python3

# add parent into python path
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

import argparse
import json

from hoopla.lib.data_loader import MovieDataLoader
from hoopla.lib.inverted_index import InvertedIndex
from hoopla.lib.keyword_search import keyword_search


def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using BM25")
    search_parser.add_argument("query", type=str, help="Search query")

    search_parser = subparsers.add_parser("build", help="Build inverted index")

    args = parser.parse_args()

    data_pool = MovieDataLoader().load()
    data_dict = {doc["id"]: doc["title"] for doc in data_pool}

    match args.command:
        case "search":
            print(f"Searching for: {args.query}")

            index = InvertedIndex()
            index.load()

            query = args.query.split()
            result_found = 0
            for query_token in query:
                doc_ids = keyword_search(index, query_token)
                for doc_id in doc_ids:
                    if result_found == 5:
                        break
                    print(f"{doc_id}, title: {data_dict[doc_id]}")
                    result_found += 1

        case "build":
            print(f"Building index")
            index = InvertedIndex()
            index.build()
            index.save()

        case _:
            parser.print_help()


if __name__ == "__main__":
    main()
