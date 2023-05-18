from django.test import TestCase
from django.urls import reverse, resolve

from .views import HomePageView
class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func.view_class,HomePageView)
from .models import Category

class CategoryModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test
        Category.objects.create(category='Innovations',
                                slug='innovations')

    def test_get_absolute_url(self):
        category=Category.objects.get(id=1)
        self.assertEquals(category.get_absolute_url(),
        '/articles/category/innovations')
