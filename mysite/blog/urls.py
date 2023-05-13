from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'blog'

urlpatterns =[
    path('', views.MainView.as_view(), name='index'),
    path('add/', views.AddCreateView.as_view(), name='add'),
    path('video_page/<int:pk>/', views.VideoDetailView.as_view(), name='video_page'),
    path('contact/', views.ContactTemplateView.as_view(), name='contact'),
    path('tag_list/', views.TagListView.as_view(), name='tag_list'),
    path('tag_detail/<int:pk>/', views.TagDetailView.as_view(), name='tag_detail'),
    path('tag_create/', views.TagCreateView.as_view(), name='tag_create'),
    path('tag_update/<int:pk>/', views.TagUpdateView.as_view(), name='tag_update'),
    path('tag_delete/<int:pk>/', views.TagDeleteView.as_view(), name='tag_delete'),
    path('video_update/<int:pk>/', views.VideoUpdateView.as_view(), name='video_update'),
    path('video_delete/<int:pk>/', views.VideoDeleteView.as_view(), name='video_delete'),
    path('user_page/<int:pk>/', views.UserDetailView.as_view(), name='user_page'),
    path('video_user_create/<int:pk>/', views.VideoUserCreateView.as_view(), name='video_user_create'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)