# -*- coding: utf-8 -*-
from django.db import models

class SearchedPhrase(models.Model):
    """
    The model for phrases searched by users
    """
    text = models.CharField(max_length=140, unique=True)
    times_searched = models.IntegerField("number of times searched", default=0)
    last_search_time = models.DateTimeField()

    def __unicode__(self):
        return self.text
