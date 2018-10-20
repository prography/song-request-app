from django.shortcuts import render, redirect, get_object_or_404
from .models import Song, Store
from .forms import SongForm

# Create your views here.
def song_list(request, pk):
    pass

def add(request, pk):
    post = get_object_or_404(Store, pk=pk)
    if request.method == "POST":
        form = SongForm(request.POST)
        if form.is_valid():
            song = form.save(commit=False)
            song.store = store
            song.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = SongForm()
    return render(request, 'main/add_comment_to_post.html', {'form': form})

def play(request, pk):
    pass

def delete_one(request, pk):
    pass

def delete_all(request, pk):
    pass

def set_delay(request, pk):
    pass

def set_site(request, pk):
    pass