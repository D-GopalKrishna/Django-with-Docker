from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView
# Create your tests here.

class HomepageTest(SimpleTestCase):
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)                    ## this self.response is accessible throughout the class

    def test_homepage_status_code(self):
        # response = self.client.get('/')
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_url_name(self):
        # response = self.client.get(reverse('home'))
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
    #    response = self.client.get('/')
       self.assertTemplateUsed(self.response, 'home.html')
    
    def test_homepage_contains_correct_html(self): # new
        # response = self.client.get('/')
        self.assertContains(self.response, 'Homepage')

    def test_homepage_does_not_contain_incorrect_html(self): # new
        # response = self.client.get('/')
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')


    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)