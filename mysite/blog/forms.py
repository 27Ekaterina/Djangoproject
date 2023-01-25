from django import forms
from django.forms import ModelForm
from .models import Video, Tag

# class ReqForm(forms.Form):
#     title = forms.CharField(label='Заголовок видео ')
#     description = forms.CharField(label='Описание видео ')
#     tag = forms.CharField(label='Теги ')


class VideoForm(ModelForm):
    class Meta:
        model = Video
        # fields = '__all__'
        fields = ['title', 'description', 'file', 'image', 'tags']
