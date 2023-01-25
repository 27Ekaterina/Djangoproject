from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'blog'

urlpatterns =[
    path('', views.main_view, name='index'),
    path('add/', views.add_new_vido, name='add'),
    path('video_page/<int:id>/', views.video_page, name='video_page'),
    path('contact/', views.contact, name='contact'),
    path('result/', views.result, name='result')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)