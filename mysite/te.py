import os
import unittest
import requests
from django.core.asgi import get_asgi_application
from django.test import TestCase

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django_asgi_app = get_asgi_application()

from proj.models import Student


class TestAPI(unittest.TestCase):
    def test_API_index(self):
        resp = requests.get("http://127.0.0.1:8000/")
        self.assertEqual(resp.status_code, 200)
        print("OK - test_API_index")

    def test_API_admin(self):
        resp = requests.get("http://127.0.0.1:8000/admin")
        self.assertEqual(resp.status_code, 200)
        print("OK - test_API_admin")

    def test_API_non_page(self):
        resp = requests.get("http://127.0.0.1:8000/non_page")
        self.assertEqual(resp.status_code, 404)
        print("OK - test_API_non_page")


class StudentModelTest(TestCase):
    def test_name_label(self):
        student = Student.objects.get(id=1)
        field_label = student._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')
        print("OK - test_name_label")

    def test_surname_label(self):
        student = Student.objects.get(id=1)
        field_label = student._meta.get_field('surname').verbose_name
        self.assertEqual(field_label, 'surname')
        print("OK - test_surname_label")

    def test_group_label(self):
        student = Student.objects.get(id=1)
        field_label = student._meta.get_field('group').verbose_name
        self.assertEqual(field_label, 'group')
        print("OK - test_group_label")

    def test_name_max_length(self):
        student = Student.objects.get(id=1)
        max_length = student._meta.get_field('name').max_length
        self.assertEqual(max_length, 50)
        print("OK - test_name_max_length - ")

    def test_surname_max_length(self):
        student = Student.objects.get(id=1)
        max_length = student._meta.get_field('surname').max_length
        self.assertEqual(max_length, 50)
        print("OK - test_surname_max_length")

    def test_group_max_length(self):
        student = Student.objects.get(id=1)
        max_length = student._meta.get_field('group').max_length
        self.assertEqual(max_length, 50)
        print("OK - test_group_max_length")


if __name__ == '__main__':
    # API
    tester_API = TestAPI()
    tester_API.test_API_index()
    tester_API.test_API_admin()
    tester_API.test_API_non_page()
    # Models
    tester = StudentModelTest()
    tester.test_name_label()
    tester.test_surname_label()
    tester.test_group_label()
    tester.test_name_max_length()
    tester.test_surname_max_length()
    tester.test_group_max_length()
