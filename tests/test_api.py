import app
import unittest


class WebAppTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.app = app.app.test_client()

    def test_user_amount(self):
        response = self.app.get("/overview/1")
        self.assertIn("John Smith".encode(), response.data)
        self.assertIn("1000".encode(), response.data)

    def test_make_payment(self):
        response = self.app.get('/choices', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn("pizza".encode(), response.data)
