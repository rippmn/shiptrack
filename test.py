from main import app
import json, time

class TestEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_discovery(self):
        response = self.app.get('/discovery')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['name'], 'shiptrack')
        self.assertEqual(data['version'], '1.0')
        self.assertEqual(data['owner'], 'lonestar')
        self.assertEqual(data['team'], 'N/A')
        self.assertEqual(data['organization'], 'acme')

    def test_liveness(self):
        response = self.app.get('/liveness')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 'live')
        self.assertEqual(data['code'], 200)
        self.assertTrue(isinstance(data['timestamp'], float))  # Check if timestamp is a float

    def test_readiness(self):
        response = self.app.get('/readiness')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 'ready')
        self.assertEqual(data['code'], 200)
        self.assertTrue(isinstance(data['timestamp'], float))  # Check if timestamp is a float


if __name__ == '__main__':
    unittest.main()
