"""urlshortener URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from shortener.views import simple
from shortener.views import get_name
from shortener.views import clement
from shortener.views import thk
from shortener.views import get_url
from shortener.views import tstCss



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/', simple),
    url(r'^name/', get_name),
    url(r'^your-name/', get_name),
    url(r'^urlAlias/', get_url),
    url(r'^thanks/', clement),
    url(r'^$', tstCss),
]
