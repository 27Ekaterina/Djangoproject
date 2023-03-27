from django.db import models
from django.core.validators import FileExtensionValidator
from usersapp.models import BlogUser

class TimeStamp(models.Model):
    '''
    Abstract - абстрактное наследование, для неё не создаются новые таблицы, данные хранятся в каждом наследнике
    '''
    create = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True



class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "tag"
        verbose_name_plural = 'tags'

class Video(TimeStamp):
    title = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(
        upload_to='video/', unique=True, blank=True, null=True,
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])]
    )
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to='poster/', null=True, blank=True)
    user = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.title

    def has_image(self):
        return bool(self.image)

    def some_method(self):
        return 'some method'

    def display_tags(self):
        tags = self.tags.all()
        result = '; '.join([item.name for item in tags])
        return result



# Классическое наследование - хранение в отдельной таблице (например name видео, name тега) со своими id
#
# class CoreObject(models.Model):
#     name = models.CharField(max_length=32)
#
# class Car(CoreObject):
#     text = models.TextField()
