from django import forms
from .models import VideoDetail

class VideoDataForm(forms.ModelForm):
    class Meta:
        model=VideoDetail
        fields=('title','description','thumbnail')
        widgets={
            'title':forms.TextInput(attrs={'class':'shadow appearance-none mb-4 border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
            'description':forms.Textarea(attrs={'class':'shadow appearance-none mb-4 border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
            'thumbnail':forms.ClearableFileInput(attrs={'class':'border-0  mb-4 outline-none'}),
        }

