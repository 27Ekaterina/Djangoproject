from django.test import TestCase
from .models import Video, Tag
from usersapp.models import BlogUser

# Библиотеки для генерации данных (основные)
# faker - простые данные, например имя
from faker import Faker
# FactoryBoy - данные для конкретной модели
# mixer - полностью создать fake модель
from mixer.backend.django import mixer

# Create your tests here.

class VideoTestCase(TestCase):

    def setUp(self):
        user = BlogUser.objects.create_user(username='testuser', email='testtest@test.ru', password='testclass')
        self.video = Video.objects.create(title='testvideo', description='some', user=user)

    def test_has_image(self):
        self.assertFalse(self.video.has_image())

    def test_some_method(self):
        video = Video.objects.get(title='testvideo')
        self.assertFalse(video.some_method() != 'some method')

    def test_str(self):
        self.assertEqual(str(self.video), 'testvideo')



class VideoTestCaseFaker(TestCase):

    def setUp(self):

        faker = Faker()
        user = BlogUser.objects.create_user(username=faker.name(), email='testtest@test.ru', password='testclass')
        self.video = Video.objects.create(title='testtitle_str', description=faker.name(), user=user)

    def test_has_image(self):

        self.assertFalse(self.video.has_image())

    def test_some_method(self):
        self.assertFalse(self.video.some_method() != 'some method')

    def test_str(self):
        self.assertEqual(str(self.video), 'testtitle_str')


class VideoTestCaseMixer(TestCase):

    def setUp(self):
        # self.video = mixer.blend(Video, title='testtitle_str')

        # print(self.video.description)
        # print(type(self.video.description))

      # хороший вариан
      #   user = mixer.blend(BlogUser, name='testuser')
      #   self.video = mixer.blend(Video, title='testtitle_str', user=user)


    # короткая запись
        self.video = mixer.blend(Video, title='testtitle_str', user__name='testuser')

    def test_has_image(self):

        self.assertFalse(self.video.has_image())

    def test_some_method(self):
        self.assertFalse(self.video.some_method() != 'some method')

    def test_str(self):
        self.assertEqual(str(self.video), 'testtitle_str')

class TagTestCase(TestCase):

    def setUp(self):
        self.tag = Tag.objects.create(name='testtag_str')

    def test_str(self):
        self.assertEqual(str(self.tag), 'testtag_str')


# class BlogUserTestCase(TestCase):
#     def setUp(self):
#         faker = Faker()
#         user = BlogUser.objects.create_user(username=faker.name(), email='testtest@test.ru', password='testclass')
#         user1 = BlogUser.objects.create_user(username=faker.name(), email='testtest@test.ru', password='testclass')
#
#     def test_bloguser(self):
#         self.assertEqual(self.user.email, self.user1.email)
