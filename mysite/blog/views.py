from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.core.files.storage import FileSystemStorage

from usersapp.models import BlogUser
from .models import Video, Tag
from .forms import VideoForm, VideoUserForm
from .management.commands.fill_db import Command
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.views.generic.base import ContextMixin


class MainView(ListView):
    paginate_by = 2
    model = Video
    template_name = 'blog/index.html'
    context_object_name = 'video'

    def get_context_data(self, *args, **kwargs):
        '''
        отвечает за передачу параметров в контекст
        :param args:
        :param kwargs:
        :return:
        '''
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        """
        Получение данных
        :return:
        """
        # return Video.objects.filter(is_active=True)
        return Video.active_objects.all()


class VideoDetailView(DetailView):
    model = Video
    template_name = 'blog/video_page.html'
    context_object_name = 'video'

    def get(self, request, *args, **kwargs):
        self.video_id = kwargs['pk']
        return super().get(request, *args, **kwargs)


class AddCreateView(LoginRequiredMixin, CreateView):
    model = Video
    form_class = VideoForm
    success_url = reverse_lazy('blog:index')
    template_name = 'blog/add.html'

    # self.request.user - текущий пользователь
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class VideoUpdateView(UserPassesTestMixin, UpdateView):
    fields = ['title', 'description', 'tags', 'image']
    model = Video
    success_url = reverse_lazy('blog:index')
    template_name = 'blog/video_update.html'

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class VideoDeleteView(UserPassesTestMixin, DeleteView):
    template_name = 'blog/video_delete_confirm.html'
    model = Video
    success_url = reverse_lazy('blog:index')
    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class ContactTemplateView(TemplateView):
    template_name = 'blog/contact.html'


class NameContextMixin(ContextMixin):

    def get_context_data(self, *args, **kwargs):
        '''
        отвечает за передачу параметров в контекст
        :param args:
        :param kwargs:
        :return:
        '''
        context = super().get_context_data(*args, **kwargs)
        context['name'] = 'Список тегов'
        return context


# список тегов

class TagListView(ListView, NameContextMixin):
    paginate_by = 4
    model = Tag
    template_name = 'blog/tag_list.html'
    context_object_name = 'tags'

    def get_queryset(self):
        """
        Получение данных
        :return:
        """
        return Tag.active_objects.all()



# детальная информация
class TagDetailView(DetailView):
    model = Tag
    template_name = 'blog/tag_detail.html'

    def get(self, request, *args, **kwargs):
        """
        метод обработки get запроса
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        self.tag_id = kwargs['pk']
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['name'] = 'Теги'
        return context

    def get_object(self, queryset=None):
        """
        получение этого объекта
        :param queryset:
        :return:
        """
        return get_object_or_404(Tag, pk=self.tag_id)


#  создание тегов

class TagCreateView(LoginRequiredMixin, CreateView):
    raise_exception = False
    # form_class =
    fields = '__all__'
    model = Tag
    success_url = reverse_lazy('blog:tag_list')
    template_name = 'blog/tag_create.html'


    # def form_valid(self, form):
    #     """
    #     срабатывает если форма валидна
    #     :param form:
    #     :return:
    #     """
    #     return super.form_valid(form)

    def post(self, request, *args, **kwargs):
        """
        Пришел пост запрос, можно из него получить данные
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().post(request, *args, **kwargs)


# обновление тега

class TagUpdateView(UserPassesTestMixin, UpdateView):
    fields = "__all__"
    model = Tag
    success_url = reverse_lazy('blog:tag_list')
    template_name = 'blog/tag_create.html'

    def test_func(self):
        return self.request.user.is_superuser

# удаление тега

class TagDeleteView(UserPassesTestMixin, DeleteView):
    template_name = 'blog/tag_delete_confirm.html'
    model = Tag
    success_url = reverse_lazy('blog:tag_list')

    def test_func(self):
        return self.request.user.is_superuser


class UserDetailView(DetailView):
    model = BlogUser
    template_name = 'blog/user_page.html'
    # def get(self, request, *args, **kwargs):
    #     """
    #     метод обработки get запроса
    #     :param request:
    #     :param args:
    #     :param kwargs:
    #     :return:
    #     """
    #     self.user_id = kwargs['pk']
    #     return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = VideoUserForm()
        return context


class VideoUserCreateView(CreateView):
    model = Video
    template_name = 'blog/user_page.html'
    success_url = '/'
    form_class = VideoUserForm

    def post(self, request, *args, **kwargs):
        self.user_pk = kwargs['pk']
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super().form_valid(form)

    # def get_success_url(self):
    #     return reverse('blog:video_user_create', kwargs={'pk': self.user_pk})

    #

