import unittest

from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider
from logic.api.api_chart_list import APIChartList


class TestApiChartList(unittest.TestCase):
    def setUp(self):
        self.api_request = APIChartList(APIWrapper())
        self.config = ConfigProvider.load_from_file()

    def test_check_chart_list(self):
        response = self.api_request.get_chart_list()
        print(response.data)
        self.assertTrue(response.ok)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data["countries"][0]["id"], "DE")
        self.assertEqual(response.data["countries"][0]["name"], "Germany")
