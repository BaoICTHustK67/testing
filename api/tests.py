from django.test import TestCase
from baowebapp.models import Student

class ModelTesting(TestCase):

    def setUp(self):
        self.student = Student.objects.create(name='bao', gender=0 , school='SOICT')

    def test_post_model(self):
        d = self.student
        self.assertTrue(isinstance(d, Student))
        self.assertEqual(str(d), 'bao')
