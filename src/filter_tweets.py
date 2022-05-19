from datetime import date
from pathlib import Path
import pickle
from tqdm import tqdm
from gpt3 import Engine
from shutil import copyfile


def get_tweet_url(tweet):
    return f'https://twitter.com/blah/status/{tweet.id}'


def print_tweet(tweet):
    return f'{tweet.user.name}\n{get_tweet_url(tweet)}\n{tweet.text}'


if __name__ == "__main__":
    tweet_path = Path('resources/tweets')
    date_string = date.today().strftime("%Y-%m-%d")
    tweet_day_path = tweet_path / f'{date_string}.tw'

    with tweet_day_path.open('rb') as f:
        tweets = pickle.load(f)

    # Filter by likes
    tweets = [tweet for tweet in tweets if tweet.favorite_count > 50]

    engine = Engine()
    output_dir = Path('output')
    output_path = output_dir / f'{date_string}.txt'
    with output_path.open('w') as f:
        for tweet in tqdm(tweets):
            if 'technical' in engine(tweet.text):
                f.write(print_tweet(tweet) + '\n\n')

    copyfile(output_path, output_dir / 'current.txt')