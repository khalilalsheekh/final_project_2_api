import unittest

from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider
from logic.api.api_shazam_songs import APIShazamSongs


class TestShazamSongs(unittest.TestCase):
    def setUp(self):
        self.api_request = APIShazamSongs(APIWrapper())
        self.config = ConfigProvider.load_from_file()

    def test_check_shazam_songs_details_by_id_and_type(self):
        querystring = self.config["query_strings"]["shazam_songs_details_query"]
        response = self.api_request.get_shazam_songs_details(querystring)
        print(response.data)
        self.assertTrue(response.ok)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data["data"][0]["id"], querystring["id"])
        self.assertEqual(response.data["data"][0]["type"], "shazam-songs")

    def test_check_shazam_songs_list_similarities(self):
        querystring = self.config["query_strings"]["shazam_songs_list_similarities_query"]
        response = self.api_request.get_shazam_songs_list_similarities(querystring)
        print(response.data)
        self.assertTrue(response.ok)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data["data"][0]["id"], querystring["id"])
        self.assertEqual(response.data["data"][0]["type"], "shazam-song-lists")
