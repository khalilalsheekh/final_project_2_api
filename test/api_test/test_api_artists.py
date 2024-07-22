import unittest

from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider
from logic.api.api_artists import APIArtists


class TestApiArtists(unittest.TestCase):
    def setUp(self):
        self.api_request = APIArtists(APIWrapper())
        self.config = ConfigProvider.load_from_file()

    def test_check_artists_details_by_id_and_type(self):
        querystring = self.config["query_strings"]["artists_query"]
        response = self.api_request.get_artists_details(querystring)
        print(response.data)
        self.assertTrue(response.ok)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data["data"][0]["id"], querystring["id"])
        self.assertEqual(response.data["data"][0]["type"], "artists")

    def test_check_artists_top_song_by_id_and_type(self):
        querystring = self.config["query_strings"]["artists_query"]
        response = self.api_request.get_artists_top_songs(querystring)
        print(response.data)
        self.assertTrue(response.ok)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data["data"][0]["id"], "850571371")
        self.assertEqual(response.data["data"][0]["type"], "songs")

    def test_check_artists_latest_release(self):
        querystring = self.config["query_strings"]["artists_query"]
        response = self.api_request.get_artists_latest_release(querystring)
        print(response.data)
        self.assertTrue(response.ok)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data["data"][0]["id"], "1673502694")
        self.assertEqual(response.data["data"][0]["type"], "albums")

    def test_check_artists_summary(self):
        querystring = self.config["query_strings"]["artists_query"]
        response = self.api_request.get_artists_summary(querystring)
        print(response.data)
        self.assertTrue(response.ok)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data["data"][0]["id"], "567072")
        self.assertEqual(response.data["data"][0]["type"], "artists")







