# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect



from .forms import NameForm


def simple(request):
    return render(request, "shortener/hello.html/", {'name': 'Buddy'})

def clement(request):
	return render(request, "shortener/clem.html/", {'nom': 'Clem', 'yourname': request.GET.get('nom', 'buddy')})

def thk(request):
	return render(request, "shortener/thk.html/")

def get_name(request):
	# import pdb; pdb.set_trace()
	if request.method == 'POST':
		form = NameForm(request.POST)

		if form.is_valid():
#			Enregister le formulaire correct
			
			return HttpResponseRedirect('/thanks/?' +  'nom=' + request.POST.get('your_name'))
	else:
		form = NameForm()

	return render(request, 'shortener/name.html/', {'form': form})

def get_url(request):
	import pdb; pdb.set_trace()
	if request.method == 'POST':
		form = UrlForm(request.POST)

		if form.is_valid():
			return HttpResponseRedirect('/urlAlias/?' + 'url=' + request.POST.get('your_url'))

	else:
		form = UrlForm()

	return render(request, 'shortener/urlAlias.html/', {'form': form})