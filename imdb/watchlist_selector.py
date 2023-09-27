#!/usr/bin/env python3

"""
Selects a random movie from your IMDb watchlist. Requires your watchlist to be made
public and the watchlist URL to be passed as an argument with the -u parameter.
"""

import argparse
import json
from random import choice

import requests
from bs4 import BeautifulSoup

from movie import Movie

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="IMDb watchlist URL", required=True)
parser.add_argument(
    "-l", "--list", help="List all movies on watchlist", action="store_true"
)
parser.add_argument(
    "-d", "--details", help="Show details for a movie", action="store_true"
)
args = parser.parse_args()


watchlist = (
    BeautifulSoup(requests.get(args.url).text, "html.parser")
    .find_all("script", type="text/javascript")[4]
    .text
)
watchlist_json = (
    watchlist.split("IMDbReactInitialState.push(")[1].strip().split(");")[0]
)
data = json.loads(watchlist_json)
movie_data = data["titles"]

movies = list()
for k, v in movie_data.items():
    movies.append(Movie(v))

if args.list:
    for movie in movies:
        if args.details:
            print(movie.full_details())
        else:
            print(movie)
else:
    movie = choice(movies)
    if args.details:
        print(movie.full_details())
    else:
        print(movie)
