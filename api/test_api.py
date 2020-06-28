from rest_framework import status
from rest_framework.test import APITestCase

class TestAPI(APITestCase):
    def test_get_customers(self):
        ''' Get list of customers '''
        response = self.client.get('/api/customers', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)