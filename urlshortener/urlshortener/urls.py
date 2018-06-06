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
from django.conf.urls.static import static
from django.conf import settings
from shortener.views import (
    get_url, get_alias, error_404,
)
from django.views.generic import RedirectView


from shortener import views as shortener_views
from django.conf.urls import handler404, handler500


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^shortener/', include('shortener.urls', namespace='shortener')),
    url(r'^$', get_url),
    url(r'^404/$', error_404),
    url(r'^urlAlias/', get_url),
    url(r'^(?P<alias>[a-z A-Z 0-9]{4})/$', get_alias),    
    url(r'^favicon\.ico$',RedirectView.as_view(url='../shortener/static/shortener/favicon.ico')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = error_404
