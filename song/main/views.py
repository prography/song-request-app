from django.shortcuts import render, redirect
from .models import *
from django.db import IntegrityError
import datetime

def index(request):
    return render(request, 'main/base.html')

def song_add(request):
    if request.method == 'GET':
        return render(request, 'main/song_add.html')
    else:
        title = request.POST.get('title')
        singer = request.POST.get('singer')
        message = request.POST.get('message')
        store_id = int(request.POST.get('store'))
        new_song = song.objects.create(title=title, singer=singer, message=message, store_id=store_id)
        return redirect("main:song_added", song_id=new_song.pk)

def song_added(request, song_id):
    context = {'song' : song.objects.get(pk=song_id)}
    return render(request, 'main/song_added.html', context)

def store_index(request, store_id):
    one_store = store.objects.get(pk=store_id)
    if one_store.reset_list != 0:
        time = datetime.datetime.now() - datetime.timedelta(hours=one_store.reset_list)
        song = one_store.song_set.filter(order_time__lte=time)
        song.filter(played=False).update(deleted=True)

    if one_store.reset_played != 0:
        time = odatetime.datetime.now() - datetime.timedelta(hours=one_store.reset_played)
        song = one_store.song_set.filter(order_time__lte=time)
        song.filter(played=True).update(deleted=True)

    context = {'song' : one_store.song_set.filter(deleted=False).filter(played=False), 'store' : one_store }
    return render(request, 'main/store_index.html', context)

def song_complited(request, store_id):
    one_store = store.objects.get(pk=store_id)
    context = {'song' : one_store.song_set.filter(deleted=False).filter(played=True), 'store' : one_store }
    return render(request, 'main/song_complited.html', context)

def song_delete(request, song_id):
    context = song.objects.get(pk=song_id)
    context.delete()
    store_id = context.store.id
    return redirect('main:store_index', store_id=store_id)

def song_all_delete(request, store_id):
    store.objects.get(pk=store_id).song_set.all().delete()
    return redirect('main:store_index', store_id=store_id)

def song_played(request, song_id):
    song.objects.filter(pk=song_id).update(played=True)
    store_id = song.objects.get(pk=song_id).store.id
    return redirect('main:store_index', store_id)

def song_return(request, song_id):
    song.objects.filter(pk=song_id).update(played=False)
    store_id = song.objects.get(pk=song_id).store.id
    return redirect('main:song_complited', store_id)

def store_set(request, store_id):
    one_store = store.objects.get(pk=store_id)

    one_store.delay = int(request.POST.get('delay'))
    one_store.site = request.POST.get('site')
    one_store.reset_list = int(request.POST.get('reset_list'))
    one_store.reset_played = int(request.POST.get('played'))

    one_store.save() 

    return redirect('main:store_index', store_id=store_id)