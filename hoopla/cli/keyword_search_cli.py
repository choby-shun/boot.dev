#!/usr/bin/env python3

# add parent into python path
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

import argparse
import json

from hoopla.lib.data_loader import MovieDataLoader
from hoopla.lib.keyword_search import keyword_search

MOVIE_PATH = "./data/movies.json"


def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using BM25")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()

    data_pool = MovieDataLoader(MOVIE_PATH).load()

    match args.command:
        case "search":
            print(f"Searching for: {args.query}")
            matches = keyword_search(data_pool, args.query)
            for index, match in enumerate(matches):
                print(f"{index}. Movie Title {match['title']}")

        case "build":
            print(f"Building index")

        case _:
            parser.print_help()


if __name__ == "__main__":
    main()
