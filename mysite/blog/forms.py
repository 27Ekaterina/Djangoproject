from django import forms
# from django.forms import ModelForm
from .models import Video, Tag


# class ReqForm(forms.Form):
#     title = forms.CharField(label='Заголовок видео ')
#     description = forms.CharField(label='Описание видео ')
#     tag = forms.CharField(label='Теги ')


class VideoForm(forms.ModelForm):
    title = forms.CharField(label='Заголовок видео ',
                            widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}))
    description = forms.CharField(label='Описание видео ',
                                  widget=forms.TextInput(attrs={'placeholder': 'Description', 'class': 'form-control'}))
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(),
                                          widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Video
        # fields = '__all__'
        # fields = ['title', 'description', 'file', 'image']
        exclude = ['tags']
