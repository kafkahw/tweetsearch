# -*- coding: utf-8 -*-
from django.shortcuts import render

from tweetsearch.utils import search_tweets, add_to_db

# Create your views here.
def search(request):
    search_dict = dict()

    if request.method == "POST":
        # form validation
        phrase = request.POST['search_phrase'].strip()
        if not phrase:
            search_dict['error_message'] = "Search box can't be blank!"
        else:
            search_dict['phrase'] = phrase
            search_dict['tweets'] = search_tweets(phrase)
            add_to_db(phrase)

    return render(request, 'tweetsearch/search.html', search_dict)
