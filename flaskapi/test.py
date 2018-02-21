import api 
import unittest
import json

class TestApi(unittest.TestCase):

    def setUp(self):
    
        self.app = api.app.test_client()
        self.app.testing = True


   
    def test_get_all(self):
        response = self.app.get('/api/v1/businesses')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['buz']), 1)

    def test_get_one(self):
        response = self.app.get('/api/v1/businesses')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['buz'][0]['buz'], 'Airtel')

    def test_item_not_exist(self):
        response = self.app.get('{}/5'.format('/api/v1/businesses'))
        self.assertEqual(response.status_code, 404)

    

    def test_delete(self):
        response = self.app.delete('{}/1'.format('/api/v1/businesses'))
        self.assertEqual(response.status_code, 204)
        response = self.app.delete('{}/5'.format('/api/v1/businesses'))
        self.assertEqual(response.status_code, 404)

    
if __name__ == "__main__":
    unittest.main()