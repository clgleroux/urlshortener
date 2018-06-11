# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import (
    render, redirect, get_object_or_404,
)


from .models import URL
from django.http import HttpRequest


from .forms import URLForm


def error_404(request):
    # Error 404 Not Found
    data = {}
    return render(request, 'shortener/error_404.html', data, status=404)


def get_url(request):

    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            # Create Alias and register
            url = form.save()
            scheme = request.is_secure() and "https" or "http"
            return render(
                request,
                'giveAlias.html',
                {
                    'url': url,
                    'my_url': scheme + '://' + HttpRequest.get_host(request)},
                status=201)
        else:
            return render(
                request,
                'shortener/urlAlias.html',
                {'form': form},
                status=400)

    else:
        form = URLForm()

    return render(request, 'shortener/urlAlias.html', {'form': form})


def get_alias(request, alias):
    # Get alias or return 404
    foo = get_object_or_404(URL, alias=alias).url
    return redirect(foo)
