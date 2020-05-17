"""
    data model tests
"""

import twitter.models as models


def test_tweet(helpers):
    tweet_data = helpers.load_json_data("testdata/models/tweet_data.json")
    tweet = models.Tweet.new_from_json_dict(tweet_data)

    assert tweet.id_str == "850006245121695744"
    assert tweet.user.id == 2244994945
    assert tweet.place.id is None
    assert tweet.entities.hashtags == []
    assert len(tweet.entities.urls) == 1


def test_quota_tweet(helpers):
    quota_tweet_data = helpers.load_json_data("testdata/models/new_quota_tweet.json")
    quota_tweet = models.Tweet.new_from_json_dict(quota_tweet_data)

    assert quota_tweet.quoted_status is not None
    assert quota_tweet.quoted_status_permalink.url == "https://t.co/LinkToTweet"


def test_retweet(helpers):
    retweet_data = helpers.load_json_data("testdata/models/retweets_data.json")
    retweet = models.Tweet.new_from_json_dict(retweet_data)

    assert retweet.retweeted_status is not None
    assert retweet.retweeted_status.text == "original message"


def test_user(helpers):
    user_data = helpers.load_json_data("testdata/models/user_data.json")
    user = models.User.new_from_json_dict(user_data)

    assert user.id == 6253282
    assert user.derived is None
    assert user.entities.url.urls[0].url == "https://t.co/8IkCzCDr19"
