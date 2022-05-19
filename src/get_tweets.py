import twitter
import pickle
from pathlib import Path
import json
from datetime import date
import time


if __name__ == "__main__":
    credentials = json.loads(Path('resources/twitter_config.json').read_text())

    api = twitter.Api(
        sleep_on_rate_limit=False,
        **credentials
    )

    tweet_path = Path('resources/tweets')
    date_string = date.today().strftime("%Y-%m-%d")
    tweet_day_path = tweet_path / f'{date_string}.tw'

    if not tweet_day_path.exists():
        all_tweets = []
        max_id = None
        now_seconds = time.time()
        while True:
            print(len(all_tweets))
            try:
                tweets = api.GetHomeTimeline(count=200, max_id=max_id, exclude_replies=True, contributor_details=True)
                max_id = min(tweet.id for tweet in tweets)
                earliest_seconds = min(tweet.created_at_in_seconds for tweet in tweets)
                all_tweets += tweets
                if now_seconds - earliest_seconds > 3600 * 24 or len(tweets) == 0:
                    break
            except Exception as e:
                print(e)
                break

        with tweet_day_path.open('wb') as f:
            pickle.dump(all_tweets, f)