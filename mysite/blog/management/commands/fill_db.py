from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def __init__(self, file, title, description, tag, image):
        super().__init__()
        self.file = file
        self.title = title
        self.description = description
        self.tag = tag
        self.image = image


    def handle(self, *args, **options):
        res = start(self.file, self.title, self.description, self.tag, self.image)
        add_video(res)
        add_tags(res)
        add_tags_for_video(res)

def start(file, title, description, tag, image):
    add_video_in_data = [file, title, description, tag, image]
    return add_video_in_data

def add_video(res):
    new_video_add = Video.objects.get_or_create(title=res[1], description=res[2], file=res[0], image=res[4])
    return new_video_add

def add_tags(res):
    for tag in res[3]:
        Tag.objects.get_or_create(name=tag)

def add_tags_for_video(res):
    for tag in res[3]:
        tag_in_new_video = Tag.objects.get(name=tag)
        result = tag_in_new_video.id
        new_video = Video.objects.get(file=res[0])
        new_video.tags.add(result)
        new_video.save()

