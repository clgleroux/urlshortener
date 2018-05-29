# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import URL, get_or_create_url

from django.test import TestCase


class TestUrl(TestCase):

    def test_creation(self):
        url = 'https://google.com'
        obj = get_or_create_url(url)
        self.assertEquals(len(obj.alias), 4)
        self.assertEquals(obj.url, url)
        self.assertEquals(URL.objects.all().count(), 1)

    def test_differents(self):
        obj1 = get_or_create_url('https://google.com')
        obj2 = get_or_create_url('https://twitter.com')
        self.assertEquals(URL.objects.all().count(), 2)
        self.assertNotEquals(obj1.alias, obj2.alias)
