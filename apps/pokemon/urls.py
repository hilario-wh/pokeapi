from django.conf.urls import include, url

from views import pokemon_list, pokemon_details, pokemon_type


urlpatterns = [
    url(r'^$', pokemon_list, name='list'),
    url(r'^/details/(?P<id>\d+)/$', pokemon_details, name='list'),
    url(r'^/type/(?P<id>\d+)/$', pokemon_type, name='list'),
]