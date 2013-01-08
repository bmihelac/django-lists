from django.conf.urls.defaults import patterns, url
from django.views.generic import ListView

from .models import Author


urlpatterns = patterns('',
        url(r'^$', ListView.as_view(model=Author)),
        )
