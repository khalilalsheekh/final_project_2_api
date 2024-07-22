import unittest

from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider
from logic.api.api_albums import APIAlbums


class TestAlbums(unittest.TestCase):
    def setUp(self):
        self.api_request = APIAlbums(APIWrapper())
        self.config = ConfigProvider.load_from_file()

    def test_check_albums_details_by_id_and_type(self):
        querystring = self.config["query_strings"]["albums_details_query"]
        response = self.api_request.get_albums_details(querystring)
        print(response.data)
        self.assertTrue(response.ok)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data["data"][0]["id"], querystring["id"])
        self.assertEqual(response.data["data"][0]["type"], "albums")


