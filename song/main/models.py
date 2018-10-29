from django.db import models

class store(models.Model):
    TYPE1 = (
        ('1', 'melon'),
        ('2', 'genie'),
        ('3', 'bugs')
    )
    name = models.CharField(max_length=100)
    delay = models.IntegerField(default=0)
    site = models.CharField(max_length=1 ,choices=TYPE1)
    reset_list = models.IntegerField(default=0)
    reset_played = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class song(models.Model):
    store = models.ForeignKey(store)
    order_time = models.DateTimeField(auto_now_add = True)
    title = models.CharField(max_length=50)
    singer = models.CharField(max_length=50)
    message = models.CharField(max_length=200, null=True)
    played = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.title