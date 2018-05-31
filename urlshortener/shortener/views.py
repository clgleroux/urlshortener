# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def simple(request):
    return render(request, "shortener/hello.html", {'name': 'Buddy'})
