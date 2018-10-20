from django import forms
from .models import Song, Store

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ('title', 'singer', 'message')