# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import (
    render, redirect, get_object_or_404,
)
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from .models import URL


from .forms import UrlForm


def error_404(request):
    data = {}
    return render(request,'shortener/error_404.html', data)

def get_url(request):
    #import pdb; pdb.set_trace()
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            URL.get_or_create(request.POST.get("your_url", "")).alias
            return HttpResponse(
                "Voici le l allias pour le lien : " + request.POST.get("your_url", "") +
                '<br /><script src="//cdnjs.cloudflare.com/ajax/libs/clipboard.js/1.4.0/clipboard.min.js"></script>' +
                '<script type="text/javascript">(function(){new Clipboard("#copy-button");})();</script>'+
                '<input id="post-shortlink" value="localhost:8000/' +
                URL.get_or_create(request.POST.get("your_url", "")).alias +
                '/"><button class="button" id="copy-button" data-clipboard-target="#post-shortlink">Copy</button>')
    
    else:
        form = UrlForm()

    return render(request, 'shortener/urlAlias.html', {'form': form})


def get_alias(request, alias):
    foo = get_object_or_404(URL, alias=alias).url
    return redirect(foo)