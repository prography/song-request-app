from django.db import models
from django.utils import timezone

# Create your models here.
class Song(models.Model):
    store = models.ForeignKey('main.Store', related_name='songs')
    created_at = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=50)
    singer = models.CharField(max_length=50)
    message = models.CharField(max_length=200)
    is_played = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)


class Store(models.Model):
    TYPE1 = (
        (1, '멜론'),
        (2, '벅스'),
    )
    store_name = models.CharField(max_length=50)
    delay = models.IntegerField()
    music_site = models.IntegerField(choices=TYPE1)