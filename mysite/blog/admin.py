from django.contrib import admin
from .models import Video, Tag


def clear_rating(modeladmin, request, queryset):
    queryset.update(rating=1)

clear_rating.short_description = 'Выставить рейтинг = 1'

class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'rating', 'user', 'display_tags']
    actions = [clear_rating]


admin.site.register(Video, VideoAdmin)

admin.site.register(Tag)

# Register your models here.
