from django.test import TestCase

# Create your tests here.

class MyTests(TestCase):
    def test_user_create(self):
        user = User.objects.create_user()
