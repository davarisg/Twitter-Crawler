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


## How to create a Twitter app

* Go to this [link](https://apps.twitter.com/) and click on `Create New App`.
* Fill in the Application.
* Twitter will then generate a consumer key and a consumer key secret for you app.
* Click on `Manage Keys and Access Tokens` and generate an access token and an access token secret.
* You can then use these keys to run the twitter crawler script.
