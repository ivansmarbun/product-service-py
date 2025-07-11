import unittest
from app import app

class TestProductService(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Product Service is running!", response.data)

    def test_get_products(self):
        response = self.app.get('/products')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)
        self.assertGreater(len(response.json), 0)

    def test_get_single_product(self):
        response = self.app.get('/products/101')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], 'Laptop')

    def test_get_non_existent_product(self):
        response = self.app.get('/products/999')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"Product not found", response.data)

if __name__ == '__main__':
    unittest.main()
