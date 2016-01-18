import unittest

from app import main_app


class AppUnitTestCases(unittest.TestCase):

    def setUp(self):
        main_app.app.config['TESTING'] = True
        self.app = main_app.app.test_client()

    def tearDown(self):
        pass

    def test_index_route(self):
        resp = self.app.get('/')
        self.assertEquals(resp.status_code, 200)
