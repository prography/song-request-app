from django.conf.urls import url
from . import views
urlpatterns = [
    #url(r'^$', views.sign_up, name='sign_up'),
    #url(r'^login/$', views.sign_in, name='sign_in'),
    url(r'^store/(?P<pk>\d+)/$', views.song_list, name='song_list'),
    url(r'^store/(?P<pk>\d+)/add/$', views.song_list, name='song_list'),
    url(r'^store/(?P<pk>\d+)/play/$', views.song_list, name='song_list'),
    url(r'^store/(?P<pk>\d+)/delete/one/$', views.delete_one, name='delete_one'),
    url(r'^store/(?P<pk>\d+)/delete/all/$', views.delete_all, name='delete_all'),
    url(r'^store/(?P<pk>\d+)/set/delay/$', views.set_delay, name='set_delay'),
    url(r'^store/(?P<pk>\d+)/set/site/$', views.set_site, name='set_site'),
]