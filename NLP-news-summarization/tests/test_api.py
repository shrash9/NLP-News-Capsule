import unittest
import json
from app import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_extractive_summarization(self):
        data = {
            'text': 'This is a sample text for testing extractive summarization.',
        }
        response = self.app.post('/extractive', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertTrue('summary' in json.loads(response.data))

    def test_abstractive_summarization(self):
        data = {
            'text': 'This is a sample text for testing abstractive summarization.',
        }
        response = self.app.post('/abstractive', data=json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertTrue('summary' in json.loads(response.data))

    def test_invalid_type(self):
        data = {
            'text': 'This is a sample text for testing an invalid endpoint.',
        }
        response = self.app.post('/invalid', data=json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()