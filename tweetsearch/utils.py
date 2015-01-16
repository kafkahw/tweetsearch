# -*- coding: utf-8 -*-
from django.conf import settings
from django.utils import timezone

from tweetsearch.models import SearchedPhrase

import tweepy

def search_tweets(phrase):
    """
    Search tweets for a given phrase and returns a list
    of SearchResult objects
    """
    consumer_key = settings.TWITTER_CONSUMER_KEY
    consumer_secret = settings.TWITTER_CONSUMER_SECRET
    access_token = settings.TWITTER_ACCESS_TOKEN
    access_token_secret = settings.TWITTER_ACCESS_TOKEN_SECRET

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    return api.search(phrase)


def add_to_db(phrase):
    """
    Adds a phrase to database if it's new, otherwise increments
    its number of searched times
    """
    try:
        existing_phrase = SearchedPhrase.objects.get(text=phrase)
    except (KeyError, SearchedPhrase.DoesNotExist):
        new_phrase = SearchedPhrase(
            text=phrase,
            times_searched=1,
            last_search_time=timezone.now()
        )
        new_phrase.save()
    else:
        existing_phrase.times_searched += 1
        existing_phrase.last_search_time = timezone.now()
        existing_phrase.save()
