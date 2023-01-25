from django.db import models
from django.core.validators import FileExtensionValidator

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    file = models.FileField(
        upload_to='video/', null=True, blank=True, unique=True,
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])]
    )
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to='poster/', null=True, blank=True)

    def __str__(self):
        return self.title


