from django.shortcuts import render, get_object_or_404
from django.core.files.storage import FileSystemStorage
from .models import Video
from .forms import VideoForm
from .management.commands.fill_db import Command
from django.http import HttpResponseRedirect


def main_view(request):
    video = Video.objects.all()
    return render(request, 'blog/index.html', context={'video': video})

def video_page(request, id):
    video_page = get_object_or_404(Video, id=id)
    return render(request, 'blog/video_page.html', context={'video_page': video_page})

def add_new_vido(request):
    form1 = VideoForm
    return render(request, 'blog/add.html', context={'form': form1})

def result(request):
    if request.method == 'POST':
        # form = ReqForm(request.POST)
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        else:
            form = VideoForm()
            return render(request, 'blog/add.html', context={'form': form})
            print("Не работает")
    else:
        form = VideoForm()
        return render(request, 'blog/add.html', context={'form': form})





        #     title = form.cleaned_data['title']
        #     description = form.cleaned_data['description']
        #     tag = form.cleaned_data['tag']
        #
        #     image_req = request.FILES["new_image"] if "new_image" in request.FILES else None
        #     if image_req:
        #         fs = FileSystemStorage('media/poster/')
        #         filename = fs.save(image_req.name, image_req)
        #         image = fs.url(filename)
        #
        #     file_req = request.FILES["new_file"] if "new_file" in request.FILES else None
        #     if file_req:
        #         fs1 = FileSystemStorage('media/video/')
        #         filename1 = fs1.save(file_req.name, file_req)
        #         file = fs1.url(filename1)
        #
        #     com = Command(file, title, description, tag, image)
        #     com.handle()
        #
        #     return render(request, 'blog/video_page1.html', context={'title': title, 'description': description, 'image': image, 'file': file})
        # else:
        #     form1 = ReqForm
        #     print("Не работает")
        #     return render(request, 'blog/add.html', context={'form': form1})

def contact(request):
    return render(request, 'blog/contact.html')


