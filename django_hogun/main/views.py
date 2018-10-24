from django.shortcuts import render, redirect, get_object_or_404
from .models import Song, Store
from .forms import SongForm


# Create your views here.
def song_list(request, pk=1):
    store = get_object_or_404(Store, pk=pk)
    songs = store.songs.all().filter(is_deleted=False, is_played=False)
    return render(request, 'main/song_list2.html', {'songs': songs, 'pk': pk})
    #return render(request, 'main/song_list.html', {'store': store})


def order_song(request, pk):
    store = get_object_or_404(Store, pk=pk)
    if request.method == "POST":
        form = SongForm(request.POST)
        if form.is_valid():
            song = form.save(commit=False)
            song.store = store
            song.is_deleted = False
            song.is_played = False
            song.save()
            return redirect('order_completed', pk=store.pk)
    else:
        form = SongForm()
    return render(request, 'main/order_song.html', {'form': form})


def order_completed(request, pk):
    store = get_object_or_404(Store, pk=pk)
    return render(request, 'main/order_completed.html', {'store': store})


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
    pass


def set_delay(request, pk):
    pass


def set_site(request, pk):
    pass
