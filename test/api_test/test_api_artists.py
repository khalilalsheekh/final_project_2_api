import unittest
import logging
from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider
from logic.api.api_artists import APIArtists

logging.basicConfig(filename='../../test_api.log', level=logging.INFO)
logger = logging.getLogger(__name__)


class TestApiArtists(unittest.TestCase):
    def setUp(self):
        self.api_request = APIArtists(APIWrapper())
        self.config = ConfigProvider.load_from_file()
        logger.info("-" * 26)

    def tearDown(self):
        self.api_request = None
        logger.info("-" * 26)

    def test_check_artists_details_by_id_and_type(self):
        """
        Test the retrieval of artist details.
        Verifies the response status, artist ID, and type.
        """
        # Arrange
        logger.info("Starting test_check_artists_details_by_id_and_type")
        querystring = self.config["query_strings"]["artists_query"]

        # Act
        response = self.api_request.get_artists_details(querystring)

        # Assert
        self.assertTrue(response.ok)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data["data"][0]["id"], querystring["id"])
        self.assertEqual(response.data["data"][0]["type"], "artists")
        logger.info("test_check_artists_details_by_id_and_type completed successfully")

    def test_check_artists_top_song_by_id_and_type(self):
        """
        Test the retrieval of an artist's top songs.
        Verifies the response status, song ID, and type.
        """
        # Arrange
        logger.info("Starting test_check_artists_top_song_by_id_and_type")
        querystring = self.config["query_strings"]["artists_query"]

        # Act
        response = self.api_request.get_artists_top_songs(querystring)

        # Assert
        self.assertTrue(response.ok)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data["data"][0]["id"], "850571371")
        self.assertEqual(response.data["data"][0]["type"], "songs")
        logger.info("test_check_artists_top_song_by_id_and_type completed successfully")

    def test_check_artists_latest_release(self):
        """
        Test the retrieval of an artist's latest release.
        Verifies the response status, album ID, and type.
        """
        # Arrange
        logger.info("Starting test_check_artists_latest_release")
        querystring = self.config["query_strings"]["artists_query"]

        # Act
        response = self.api_request.get_artists_latest_release(querystring)

        # Assert
        self.assertTrue(response.ok)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data["data"][0]["id"], "1673502694")
        self.assertEqual(response.data["data"][0]["type"], "albums")
        logger.info("test_check_artists_latest_release completed successfully")

    def test_check_artists_summary(self):
        """
        Test the retrieval of an artist's summary.
        Verifies the response status, artist ID, and type.
        """
        # Arrange
        logger.info("Starting test_check_artists_summary")
        querystring = self.config["query_strings"]["artists_query"]

        # Act
        response = self.api_request.get_artists_summary(querystring)

        # Assert
        self.assertTrue(response.ok)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data["data"][0]["id"], "567072")
        self.assertEqual(response.data["data"][0]["type"], "artists")
        logger.info("test_check_artists_summary completed successfully")
