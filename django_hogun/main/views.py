from django.shortcuts import render, redirect, get_object_or_404
from .models import Song, Store
from django.utils import timezone
from .forms import SongForm


# Create your views here.
def song_list(request, pk=1):
    store = get_object_or_404(Store, pk=pk)
    if store.period_order > 0:
        time_from = timezone.now() - timezone.timedelta(hours=store.period_order)
        songs = store.songs.all().filter(is_deleted=False, is_played=False, created_at__gte=time_from).order_by('-created_at')
    else:
        songs = store.songs.all().filter(is_deleted=False, is_played=False).order_by('-created_at')

    url1 = ''
    url2 = ''
    if store.music_site == 1:
        url1 = "https://www.melon.com/search/total/index.htm?q="
        url2 = "&section=&searchGnbYn=Y&kkoSpl=Y&kkoDpType=&linkOrText=T&ipath=srch_form"
    elif store.music_site == 2:
        url1 = "http://www.genie.co.kr/search/searchMain?query="
        url2 = ""
    elif store.music_site == 3:
        url1 = "https://music.bugs.co.kr/search/integrated?q="
        url2 = ""

    return render(request, 'main/host-home-window.html', {'store': store, 'songs': songs, 'url1': url1, 'url2': url2, 'pk': pk})


def complete_list(request, pk=1):
    store = get_object_or_404(Store, pk=pk)
    if store.period_complete > 0:
        time_from = timezone.datetime.now() - timezone.timedelta(hours=store.period_complete)
        print(time_from)
        songs = store.songs.all().filter(is_deleted=False, is_played=True, created_at__gte=time_from).order_by('-created_at')
    else:
        songs = store.songs.all().filter(is_deleted=False, is_played=True).order_by('-created_at')
    return render(request, 'main/host-end-request-window.html', {'store':store, 'songs': songs, 'pk': pk})


def delete_list(request, pk=1):
    store = get_object_or_404(Store, pk=pk)
    songs = store.songs.all().filter(is_deleted=True, is_played=False).order_by('-created_at')
    return render(request, 'main/complete_list.html', {'songs': songs, 'pk': pk})


def order_song(request, pk):
    store = get_object_or_404(Store, pk=pk)
    if request.method == "POST":
        print(request.POST)
        title = request.POST.get('title')
        singer = request.POST.get('singer')
        message = request.POST.get('message')
        print('-----------------------------')
        print(title)
        print(singer)
        print(message)
        print('-----------------------------')

        if title and singer: # and message:
            song = Song.objects.create(store=store, title=title, singer=singer, message=message)
            song.save()
            return redirect('order_completed', pk=song.pk)
        else:
            print("Wrong Field Values")
            return render(request, 'main/guest-request-start-window.html')
    return render(request, 'main/guest-request-start-window.html')


def order_completed(request, pk):
    song = get_object_or_404(Song, pk=pk)
    return render(request, 'main/guest-request-end-window.html', {'song': song})


def play_song(request, pk):
    song = get_object_or_404(Song, pk=pk)
    song.is_played = True
    song.save()
    return redirect('song_list', pk=song.store.pk)


def delete_one(request, pk):
    song = get_object_or_404(Song, pk=pk)
    song.is_deleted = True
    song.save()
    return redirect('song_list', pk=song.store.pk)


def delete_all(request, pk):
    store = get_object_or_404(Store, pk=pk)
    songs = store.songs.all().filter(is_deleted=False, is_played=False)
    songs.update(is_deleted=True)
    return redirect('song_list', pk=pk)


def restore_one(request, pk):
    song = get_object_or_404(Song, pk=pk)
    song.is_played = False
    song.is_deleted = False
    song.save()
    return redirect('complete_list', pk=song.store.pk)


def set_settings(request, pk):
    store = get_object_or_404(Store, pk=pk)
    #if request.method=='POST':
    delay_time = request.POST.get('delay_time')
    music_site = request.POST.get('music_site')
    period_order = request.POST.get('period_order')
    period_complete = request.POST.get('period_complete')

    print('=-=-=--=-=-=-=--=-=-=-=--=-=-=-=--=-=-=-=--=')
    print(delay_time)
    print(music_site)
    print(period_order)
    print(period_complete)
    print('=-=-=--=-=-=-=--=-=-=-=--=-=-=-=--=-=-=-=--=')
    update_fields = []
    if delay_time:
        store.delay_time = delay_time
        update_fields.append('delay_time')
    if music_site:
        store.music_site = music_site
        update_fields.append('music_site')
    if period_order:
        store.period_order = period_order
        update_fields.append('period_order')
    if period_complete:
        store.period_complete = period_complete
        update_fields.append('period_complete')

    store.save(update_fields=update_fields)
    return redirect('song_list', pk=store.pk)
