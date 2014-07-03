from django.conf.urls import patterns, include, url

from url_shortener.views import URLViewSet

urlpatterns = patterns('',
    url(r'^$', URLViewSet, base_name='api_url'),
)
