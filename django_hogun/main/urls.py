from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.sign_up, name='sign_up'),
    # url(r'^login/$', views.sign_in, name='sign_in'),
    url(r'^$', views.song_list, name='first_store'),
    url(r'^store/(?P<pk>\d+)/list/$', views.song_list, name='song_list'),
    url(r'^store/(?P<pk>\d+)/list/complete/$', views.complete_list, name='complete_list'),
    url(r'^store/(?P<pk>\d+)/list/delete/$', views.delete_list, name='delete_list'),
    url(r'^store/(?P<pk>\d+)/song/order/$', views.order_song, name='order_song'),
    url(r'^song/complete/(?P<pk>\d+)/$', views.order_completed, name='order_completed'),
    url(r'^song/play/(?P<pk>\d+)$', views.play_song, name='play_song'),
    url(r'^delete/one/(?P<pk>\d+)/$', views.delete_one, name='delete_one'),
    url(r'^restore/one/(?P<pk>\d+)/$', views.restore_one, name='restore_one'),
    url(r'^store/(?P<pk>\d+)/delete/all/$', views.delete_all, name='delete_all'),
    url(r'^store/(?P<pk>\d+)/setting/$', views.set_settings, name='set_settings'),
]
