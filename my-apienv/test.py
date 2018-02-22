from api.views import register, login, logout, reset_password, business_update, remove_business,  One_business, All_business
import unittest
import json
from api.models import User , Business

class TestApi(unittest.TestCase):

    def setUp(self):
        self.app = login()

    def test_login_endpoint(self):
        response = self.app.post('/api/v1/auth/login')
        self.assertEqual(response.status_code, 200)

class TestApi1(unittest.TestCase):

    def setUp(self):
        self.app = logout()

    def test_logout_endpoint(self):
        response = self.app.post('/api/v1/auth/logout')
        self.assertEqual(response.status_code, 200)

class TestApi2(unittest.TestCase):

    def setUp(self):
        self.app = register()

    def test_register_user_endpoint(self):
        response = self.app.post('/api/v1/auth/register')
        self.assertEqual(response.status_code, 200)

class TestApi3(unittest.TestCase):

    def setUp(self):
        self.app = reset_password()

    def test_password_reset_endpoint(self):
        response = self.app.post('/api/v1/auth/reset-password')
        self.assertEqual(response.status_code, 200)

class TestApi4(unittest.TestCase):

    def setUp(self):
        self.app = All_business()

    def test_show_all_businesses(self):
        response = self.app.get('/api/v1/businesses')
        self.assertEqual(response.status_code, 200)

class TestApi5(unittest.TestCase):

    def setUp(self):
        self.app = One_business(1)

    def test_show_one_business(self):
        response = self.app.get('/api/v1/businesses/1')
        self.assertEqual(response.status_code, 200)

class TestApi6(unittest.TestCase):

    def setUp(self):
        self.app = remove_business(1)

    def test_delete(self):
        response = self.app.delete('{}/1'.format('/api/v1/businesses'))
        self.assertEqual(response.status_code, 200)
        

    
if __name__ == "__main__":
    unittest.main()
