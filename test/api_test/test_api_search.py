import unittest

from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider
from logic.api.api_search import APISearch


class TestApiSearch(unittest.TestCase):
    def setUp(self):
        self.api_request = APISearch(APIWrapper())
        self.config = ConfigProvider.load_from_file()

    def test_check_search(self):
        querystring = self.config['query_strings']['search_query']
        response = self.api_request.get_search(querystring)
        print(response.data)
        self.assertTrue(response.ok)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data["tracks"]["hits"][0]["track"]["subtitle"], "Billie Myers")
        self.assertEqual(response.data["tracks"]["hits"][0]["track"]["title"], "Kiss the Rain")


