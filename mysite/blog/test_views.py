from django.test import Client
from django.test import TestCase
from django.urls import reverse
from faker import Faker
from usersapp.models import BlogUser
from .models import Video
from mixer.backend.django import mixer


class ViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.fake = Faker()

    def test_statuses(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

        # post запрос
        response = self.client.post('/tag_create/', {'name': self.fake.name()})
        self.assertEqual(response.status_code, 302)

        # какие данные передаются в контексте
        response = self.client.get('/')
        self.assertTrue('video' in response.context)
        # response.context[]

    def test_login_required(self):
        user = BlogUser.objects.create_user(username='test_user', email='testtest@test.ru', password='testclass')
        # он не вошел
        response = self.client.get('/add/')
        self.assertEqual(response.status_code, 302)

        # логиним
        self.client.login(username='test_user', password='testclass')
        response = self.client.get('/add/')
        self.assertEqual(response.status_code, 200)

    # def test_update(self):
    #     user = BlogUser.objects.create_user(username='test_user', email='testtest@test.ru', password='testclass')
    #     response = self.client.get('/video_update/')
    #     self.assertEqual(response.status_code, 302)


class VideoDetailViewTestCase(TestCase):

    def setUp(self):
        # faker = Faker()
        # user = BlogUser.objects.create_user(username=faker.name(), email='testtest@test.ru', password='testclass')
        # self.video = Video.objects.create(title='testtitle_str', description=faker.name(), file='video/АВРОРА.mp4', user=user)
        # self.video2 = Video.objects.create(title='testtitle_str2', description=faker.name(), file='video/АВРОРА2.mp4',
        #                                   user=user)
        self.video = mixer.blend(Video, file='video/АВРОРА.mp4')

    def test_detail_video(self):
        response = self.client.get('/video_page/1/')
        self.assertEqual(response.status_code, 200)
        
