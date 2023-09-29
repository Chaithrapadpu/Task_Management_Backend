from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

class RegisterAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_successful_registration(self):
    registration_data = {
        'username': 'testuser',
        'password': 'testpassword',
        'confirm_password': 'testpassword',
    }

    response = self.client.post('/register/', data=registration_data, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    try:
        new_user = User.objects.get(username='testuser')
        self.assertIsNotNone(new_user)
        self.assertTrue(new_user.check_password('testpassword'))
    except User.DoesNotExist:
        self.fail("User was not created successfully.")


    def test_registration_with_mismatched_passwords(self):
        registration_data = {
            'username': 'testuser',
            'password': 'testpassword',
            'confirm_password': 'mismatchedpassword',
        }

        response = self.client.post('/register/', data=registration_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        with self.assertRaises(User.DoesNotExist):
            User.objects.get(username='testt')


            

    
