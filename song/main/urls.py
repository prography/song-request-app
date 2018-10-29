from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^song/add/$', song_add, name="song_add"),
    url(r'^song/added/(?P<song_id>\d+)/$', song_added, name="song_added"),

    url(r'^store/(?P<store_id>\d+)/$', store_index, name="store_index"),
    
    url(r'^song/completed/(?P<store_id>\d+)/$', song_completed, name="song_completed"),

    url(r'^song/delete/(?P<song_id>\d+)/$', song_delete, name='song_delete'),
    url(r'^(?P<store_id>\d+)/song/all_delete/$', song_all_delete, name='song_all_delete'),
    url(r'^song/played/(?P<song_id>\d+)/$', song_played, name='song_played'),
    url(r'^song/return/(?P<song_id>\d+)/$', song_return, name='song_return'),
    
    url(r'^store/set/(?P<store_id>\d+)/$', store_set, name="store_set"),
]