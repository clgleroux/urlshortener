# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import base64
import hashlib
from urllib.parse import urlparse

from django.db import models


class URL(models.Model):
    url = models.TextField()
    alias = models.CharField(max_length=4, primary_key=True)

    @classmethod
    def get_or_create(cls, url):
        # create an SHA1 for the current url
        hasher = hashlib.sha1(url.encode())
        # Alias should be 4 character long
        alias = base64.urlsafe_b64encode(hasher.digest())[0:4]

        # retieve URL object from db if exists to avoid colision
        obj, _ = cls.objects.get_or_create(alias=alias)

        # Don't update if same url is given
        if url != obj.url:
            obj.url = url
            obj.save()

        # Return current instance, hope it will be usefull :D
        return obj

    def __str__(self):
        return '{} - {}'.format(self.alias, urlparse(self.url).hostname)
