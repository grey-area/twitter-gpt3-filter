#!/bin/bash

set -e

python src/get_tweets.py
python src/filter_tweets.py
less output/current.txt