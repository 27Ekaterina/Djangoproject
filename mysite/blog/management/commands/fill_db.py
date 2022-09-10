import pprint
import json
from django.core.management.base import BaseCommand
from blog.models import Video, Tag


new_file = 'УЛИЧНЫЕ МУЗЫКАНТЫ.mp4'
new_title = 'уличные музыканты'
new_description = 'уличные музыканты, Москва'
new_tag = ["уличные", "музыканты", 'Москва']
add_video = [new_file, new_title, new_description, new_tag]


FILE_NAME = "new_video.json"
with open(FILE_NAME, 'w') as f:
    json.dump(add_video, f)

with open(FILE_NAME) as f:
    add_video_in_data = json.load(f)


def add_video(add_video_in_data):
    new_video_add = Video.objects.get_or_create(title=add_video_in_data[1], description=add_video_in_data[2], file=add_video_in_data[0])
    return new_video_add

def add_tags(add_video_in_data):
    for tag in add_video_in_data[3]:
        Tag.objects.get_or_create(name=tag)

def add_tags_for_video(add_video_in_data):
    for tag in add_video_in_data[3]:
        tag_in_new_video = Tag.objects.get(name=tag)
        result = tag_in_new_video.id
        new_video = Video.objects.get(file=add_video_in_data[0])
        new_video.tags.add(result)
        new_video.save()

class Command(BaseCommand):
    def handle(self, *args, **options):
        add_video(add_video_in_data)
        add_tags(add_video_in_data)
        add_tags_for_video(add_video_in_data)
