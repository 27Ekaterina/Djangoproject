from django.contrib import admin
from django.db.models import F

from .models import Video, Tag


def clear_rating(modeladmin, request, queryset):
    queryset.update(rating=1)

def set_active(modeladmin, request, queryset):

    # bulk update (пакетный)
    queryset.update(is_active=True)

#  поменять активные на неактивные
def reverse_is_active(modeladmin, request, queryset):
    # в цикле будет долго обрабатывать
    for item in queryset:
        item.is_active = not item.is_active
        item.save()
#
#     # bulk update (пакетный)
#     # F объект
#     queryset.update(is_active=False if F('is_active') == True else True)

# рейтинг +=1
def add_rating(modeladmin, request, queryset):
    # в цикле будет долго обрабатывать
    # for item in queryset:
    #     item.rating +=1
    #     item.save()

    # bulk update (пакетный)
    # F объект
    queryset.update(rating=F('rating') + 1)

clear_rating.short_description = 'Выставить рейтинг = 1'

class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'rating', 'user', 'display_tags', 'is_active']
    actions = [clear_rating, set_active, reverse_is_active, add_rating]

class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    actions = [set_active]


admin.site.register(Video, VideoAdmin)

admin.site.register(Tag, TagAdmin)

# Register your models here.
