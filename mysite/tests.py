import unittest
import requests

class TestAPI(unittest.TestCase):

    def test1(self):
        resp = requests.get("http://127.0.0.1:8000/")
        self.assertEqual(resp.status_code, 200)
        print("test1: OK")

    def test2(self):
        resp = requests.get("http://127.0.0.1:8000/admin")
        self.assertEqual(resp.status_code, 200)
        print("test2: OK")

    def test3(self):
        resp = requests.get("http://127.0.0.1:8000/non_page")
        self.assertEqual(resp.status_code, 404)
        print("test2: OK")


if __name__ == '__main__':
    tester = TestAPI()
    tester.test1()
    tester.test2()
    tester.test3()