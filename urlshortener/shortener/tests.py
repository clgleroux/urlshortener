# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import URL
from django.urls import reverse

from django.test import TestCase


class TestUrl(TestCase):

    def test_creation(self):
        url = 'https://google.com'
        obj = URL.get_or_create(url)
        self.assertEquals(len(obj.alias), 4)
        self.assertEquals(obj.url, url)
        self.assertEquals(URL.objects.all().count(), 1)

    def test_differents(self):
        obj1 = URL.get_or_create('https://google.com')
        obj2 = URL.get_or_create('https://twitter.com')
        self.assertEquals(URL.objects.all().count(), 2)
        self.assertNotEquals(obj1.alias, obj2.alias)

    def test_form_exists(self):
        url = reverse("url-form")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_form_valide(self):
        url = reverse("url-form")
        response = self.client.post(url, {"your_url": "http://google.com"})
        self.assertEquals(response.status_code, 201)

    def test_form_invalid(self):
        url = reverse("url-form")
        response = self.client.post(url, {})
        self.assertEquals(response.status_code, 400)

    def test_redirect_valid(self):
        target = 'https://twitter.com'
        obj = URL.get_or_create(target)
        url = reverse("redirect", kwargs={"alias": obj.alias})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, target)

    def test_redirect_invalid(self):
        url = reverse("redirect", kwargs={"alias": "Fake"})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_page404(self):
        url = reverse("error-404")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)
