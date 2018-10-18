from django.db import models
from django.utils import timezone

# Create your models here.
class Song(models.Model):
    store = models.ForeignKey('main.Store')
    time = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=20)
    singer = models.CharField(max_length=20)
    message = models.TextField()
    play = models.BooleanField(default=False)
    delete = models.BooleanField(default=False)


class Store(models.Model):
    delay = models.IntegerField()
    site = models.CharField(max_length=10)