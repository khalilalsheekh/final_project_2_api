import unittest
import logging
from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider
from logic.api.api_songs import APISongs
from test.api_test.utils import get_sound_file

logging.basicConfig(filename='../../test_api.log', level=logging.INFO)
logger = logging.getLogger(__name__)


class TestApiSongs(unittest.TestCase):
    def setUp(self):
        self.api_request = APISongs(APIWrapper())
        self.config = ConfigProvider.load_from_file()
        logger.info("-" * 26)

    def tearDown(self):
        self.api_request = None
        logger.info("-" * 26)

    def test_check_songs_details(self):
        """
        Test the retrieval of song details.
        Verifies the response status, song ID, type, and artist name.
        """
        logger.info("Starting test_check_songs_details")
        querystring = self.config["query_strings"]["songs_query_details"]
        response = self.api_request.get_songs_details(querystring)
        self.assertTrue(response.ok)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data["data"][0]["id"], querystring["id"])
        self.assertEqual(response.data["data"][0]["type"], "songs")
        self.assertEqual(response.data["data"][0]["attributes"]["artistName"], "Gorillaz")
        logger.info("test_check_songs_details completed successfully")

    def test_related_artist(self):
        """
        Test the retrieval of related artists.
        Verifies the response status and the ID of the first related artist.
        """
        logger.info("Starting test_related_artist")
        querystring = self.config["query_strings"]["songs_related_artists_query"]
        response = self.api_request.get_related_artist(querystring)
        self.assertTrue(response.ok)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data["data"][0]["id"], "567072")
        logger.info("test_related_artist completed successfully")

    def test_check_songs_count(self):
        """
        Test the retrieval of song count for a specific tag.
        Verifies the response status, tag ID, and type.
        """
        logger.info("Starting test_check_songs_count")
        querystring = self.config["query_strings"]["count_query"]
        response = self.api_request.get_songs_count(querystring)
        self.assertTrue(response.ok)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data["id"], "40333609")
        self.assertEqual(response.data["type"], "tag")
        logger.info("test_check_songs_count completed successfully")

    def test_check_specific_song_details(self):
        """
        Test the retrieval of specific song details.
        Verifies the response status, song key, title, and subtitle.
        """
        logger.info("Starting test_check_specific_song_details")
        querystring = self.config["query_strings"]["specific_details_query"]
        response = self.api_request.get_specific_song_details(querystring)
        self.assertTrue(response.ok)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data["key"], "40333609")
        self.assertEqual(response.data["title"], "River Flows In You")
        self.assertEqual(response.data["subtitle"], "Yiruma")
        logger.info("test_check_specific_song_details completed successfully")

    def test_check_songs_v2_detect_post(self):
        """
        Test the song detection feature using audio data.
        Verifies the response status and detected song title.
        """
        logger.info("Starting test_check_songs_v2_detect_post")
        self.sound_data = get_sound_file()
        querystring = self.config["query_strings"]["sound_detector_v2_query"]
        response = self.api_request.post_songs_v2_detect(querystring, self.sound_data)
        self.assertTrue(response.ok)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data["track"]["title"], "Clint Eastwood")
        logger.info("test_check_songs_v2_detect_post completed successfully")
