from django.shortcuts import render, redirect, get_object_or_404
from .models import Song, Store
from .forms import SongForm

# Create your views here.
def song_list(request, pk):
    pass

def order_song(request, pk):
    store = get_object_or_404(Store, pk=pk)
    if request.method == "POST":
        form = SongForm(request.POST)
        if form.is_valid():
            song = form.save(commit=False)
            song.store = store
            song.save()
            return render(request, 'main/order_completed.html', {'store': store})
            #return redirect('order_completed', pk=post.pk)
    else:
        form = SongForm()
    return render(request, 'main/order_song.html', {'form': form})

def order_completed(request, pk):
    store = get_object_or_404(Store, pk=pk)
    return render(request, 'main/order_song.html', {'store': store})

def play_song(request, pk):
    pass

def delete_one(request, pk):
    pass

def delete_all(request, pk):
    pass

def set_delay(request, pk):
    pass

def set_site(request, pk):
    pass