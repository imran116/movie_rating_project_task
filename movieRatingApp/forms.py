from django import forms
from .models import AddMovie


class AddMovieForm(forms.ModelForm):
    class Meta:
        model = AddMovie
        fields = ('name', 'genre', 'rating', 'release_date')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter Movie name'}),
            'genre': forms.TextInput(attrs={'placeholder': 'eg. Crime,Action'}),
            'rating': forms.TextInput(attrs={'placeholder': 'eg. PG,R'}),
            'release_date': forms.TextInput(attrs={'placeholder': 'Enter release date: dd-mm-yyyy'}),
        }
