from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Page

class LandingPageAPITest(APITestCase):
    def setUp(self):
        self.page = Page.objects.create(title="Accueil", slug="accueil", published=True)

    def test_landing_page_endpoint(self):
        url = reverse('landing-page-api', kwargs={'slug': 'accueil'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('sections', response.data)

