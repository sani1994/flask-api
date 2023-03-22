import unittest
from app import app


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_rates(self):
        expected_data = b'[{"average_price":882,"day":"2016-01-01"},{"average_price":882,"day":"2016-01-02"},' \
                        b'{"average_price":882,"day":"2016-01-05"},{"average_price":882,"day":"2016-01-06"},' \
                        b'{"average_price":882,"day":"2016-01-07"},{"average_price":832,"day":"2016-01-08"},' \
                        b'{"average_price":832,"day":"2016-01-09"},{"average_price":832,"day":"2016-01-10"},' \
                        b'{"average_price":832,"day":"2016-01-11"},{"average_price":832,"day":"2016-01-12"},' \
                        b'{"average_price":832,"day":"2016-01-13"},{"average_price":832,"day":"2016-01-14"},' \
                        b'{"average_price":832,"day":"2016-01-15"},{"average_price":832,"day":"2016-01-16"},' \
                        b'{"average_price":832,"day":"2016-01-17"},{"average_price":832,"day":"2016-01-18"},' \
                        b'{"average_price":832,"day":"2016-01-19"},{"average_price":832,"day":"2016-01-20"},' \
                        b'{"average_price":832,"day":"2016-01-21"},{"average_price":832,"day":"2016-01-22"},' \
                        b'{"average_price":832,"day":"2016-01-23"},{"average_price":815,"day":"2016-01-24"},' \
                        b'{"average_price":815,"day":"2016-01-25"},{"average_price":815,"day":"2016-01-26"},' \
                        b'{"average_price":815,"day":"2016-01-27"},{"average_price":815,"day":"2016-01-28"},' \
                        b'{"average_price":798,"day":"2016-01-29"},{"average_price":798,"day":"2016-01-30"}]'
        response = self.app.get(
            '/rates?date_from=2016-01-01&date_to=2016-01-30&origin=CNSGH&destination=north_europe_main')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.rstrip(b'\n'), expected_data)

    def test_price_without_parameter(self):
        expected_data = b'[{"error":"Parameter missing: origin/destination/date_to/date_from"}]'
        response = self.app.get('/rates', data={})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.rstrip(b'\n'), expected_data)

    def test_invalid_path(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 404)
