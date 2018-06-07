# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import (
    render, redirect, get_object_or_404,
)


from .models import URL
from django.http import HttpRequest


from .forms import UrlForm


def error_404(request):
    data = {}
    return render(request, 'shortener/error_404.html', data, status=404)


def get_url(request):
    # import pdb; pdb.set_trace()
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            your_url = request.POST.get('your_url', '')
            url = URL.get_or_create(your_url)
            scheme = request.is_secure() and "https" or "http"
            return render(
                request,
                'giveAlias.html',
                {
                    'url': url,
                    'your_url': your_url,
                    'my_url': scheme + '://' + HttpRequest.get_host(request)},
                status=201)
        else:
            return render(
                request,
                'shortener/urlAlias.html',
                {'form': form},
                status=400)

    else:
        form = UrlForm()

    return render(request, 'shortener/urlAlias.html', {'form': form})


def get_alias(request, alias):
    foo = get_object_or_404(URL, alias=alias).url
    return redirect(foo)
