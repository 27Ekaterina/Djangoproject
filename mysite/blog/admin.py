from django.contrib import admin
from .models import Video, Tag


def clear_rating(modeladmin, request, queryset):
    queryset.update(rating=1)

def set_active(modeladmin, request, queryset):
    queryset.update(is_active=True)

clear_rating.short_description = 'Выставить рейтинг = 1'

class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'rating', 'user', 'display_tags', 'is_active']
    actions = [clear_rating, set_active]

class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    actions = [set_active]


admin.site.register(Video, VideoAdmin)

admin.site.register(Tag, TagAdmin)

# Register your models here.
