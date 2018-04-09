# Twitter Crawler

A Twitter Crawler that follows specific accounts and stores data from their tweets in a CSV file.

## How to setup on a server

* Create a virtualenv `virtualenv -p python3 venv`
* Load the virtualenv `source venv/bin/activate`
* Install the necessary packages `pip install -r requirements.txt`


## How to run the script

```
python twitter_crawler.py --consumer-key=yourconsumerkey --consumer-secret=yourconsumersecret --access-token=youraccesstoken --access-token-secret=youraccesstokensecret
```


The script also optionally takes 2 more flags:

```
--accounts=FCAugburg Herta LFC
--csv-file=pathtocsvfile.csv
```

Use `python twitter_crawler.py --help` for help with the flags.
