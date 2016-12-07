from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase
# Create your tests here.
from rest_framework.authtoken.models import Token


class RecruiterTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user('testuser', email='testuser@test.com', password='testing')
        self.user.save()
        token = Token.objects.create(user=self.user)
        token.save()




    def _require_login(self):
        self.client.login(username='testuser', password='testing')
        self.client.force_authenticate(user=self.user)

    def test_get_recruiter(self):

        url = reverse('contact-list')
        response = self.client.get(url)

        # Access Denied
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

        self._require_login()
        print(self.user.is_authenticated())
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_recruiter(self):
        pass