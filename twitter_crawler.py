import argparse
import csv
import tweepy


FOLLOWED_TWITTER_ACCOUNT_USERNAMES = [
    'FCAugsburg',
    'HerthaBSC',
    'werderbremen'
]


class CSVStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        with open('tweets.csv', 'a') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([
                status.id,
                status.user.id,
                status.user.screen_name in FOLLOWED_TWITTER_ACCOUNT_USERNAMES,
                status.text.replace('\n', '\\n'),
                True if hasattr(status, 'retweeted_status') else False,
                ", ".join(["#%s" % hashtag['text'] for hashtag in status.entities['hashtags']]),
                ", ".join(["@%s" % user_mention['screen_name'] for user_mention in status.entities['user_mentions']])
            ])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Twitter Crawler')
    parser.add_argument(
        '--accounts',
        dest='accounts',
        nargs='+',
        help='A space separated list of twitter usernames',
        default=FOLLOWED_TWITTER_ACCOUNT_USERNAMES
    )
    parser.add_argument(
        '--csv-file',
        dest='csv_filename',
        type=str,
        default='tweets.csv',
        help='The name of the CSV file to write tweets'
    )
    parser.add_argument('--consumer-key', dest='consumer_key', type=str, required=True)
    parser.add_argument('--consumer-secret', dest='consumer_secret', type=str, required=True)
    parser.add_argument('--access-token', dest='access_token', type=str, required=True)
    parser.add_argument('--access-token-secret', dest='access_token_secret', type=str, required=True)
    args = parser.parse_args()

    auth = tweepy.OAuthHandler(args.consumer_key, args.consumer_secret)
    auth.set_access_token(args.access_token, args.access_token_secret)

    api = tweepy.API(auth)

    with open('tweets.csv', 'w', newline='\n') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([
            'Tweet ID',
            'User ID',
            'Posted from Followed Account',
            'Text',
            'Is Retweet',
            'Hashtags',
            'User Mentions'
        ])

    csv_stream = tweepy.Stream(auth=api.auth, listener=CSVStreamListener())

    csv_stream.filter(follow=[
        str(api.get_user(username).id)
        for username in args.accounts
    ])
