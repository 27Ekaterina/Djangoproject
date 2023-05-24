from mixer.backend.django import mixer
from django.core.management.base import BaseCommand
from blog.models import Video, Tag

class Command(BaseCommand):
    def handle(self, *args, **options):
        count = 10
        for i in range(count):
            p = (i/count)*100
            print(f'{i} {p} %')
            mixer.blend(Video)
        print('end')

