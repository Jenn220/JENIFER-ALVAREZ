import unittest
from aplicacion import app  

class TestApp(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hola', response.data)
    
    def test_suma(self):
        response = self.app.get('/suma/5/3')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'8', response.data)
    
    def test_resta(self):
        response = self.app.get('/resta/10/4')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'6', response.data)
    
    def test_suma_negativos(self):
        response = self.app.get('/suma/-5/3')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'-2', response.data)

if __name__ == '__main__':
    unittest.main()