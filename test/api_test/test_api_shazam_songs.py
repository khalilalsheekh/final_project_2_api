import unittest
import logging
from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider
from logic.api.api_shazam_songs import APIShazamSongs

logging.basicConfig(filename='../../test_api.log', level=logging.INFO)
logger = logging.getLogger(__name__)


class TestShazamSongs(unittest.TestCase):
    def setUp(self):
        self.api_request = APIShazamSongs(APIWrapper())
        self.config = ConfigProvider.load_from_file()
        logger.info("-" * 26)

    def tearDown(self):
        self.api_request = None
        logger.info("-" * 26)

    def test_check_shazam_songs_details_by_id_and_type(self):
        """
        Test the retrieval of Shazam song details.
        Verifies the response status, song ID, and type.
        """
        # Arrange
        logger.info("Starting test_check_shazam_songs_details_by_id_and_type")
        querystring = self.config["query_strings"]["shazam_songs_details_query"]

        # Act
        response = self.api_request.get_shazam_songs_details(querystring)

        # Assert
        self.assertTrue(response.ok)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data["data"][0]["id"], querystring["id"])
        self.assertEqual(response.data["data"][0]["type"], "shazam-songs")
        logger.info("test_check_shazam_songs_details_by_id_and_type completed successfully")

    def test_check_shazam_songs_list_similarities(self):
        """
        Test the retrieval of similar Shazam songs.
        Verifies the response status, song list ID, and type.
        """
        # Arrange
        logger.info("Starting test_check_shazam_songs_list_similarities")
        querystring = self.config["query_strings"]["shazam_songs_list_similarities_query"]

        # Act
        response = self.api_request.get_shazam_songs_list_similarities(querystring)

        # Assert
        self.assertTrue(response.ok)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data["data"][0]["id"], querystring["id"])
        self.assertEqual(response.data["data"][0]["type"], "shazam-song-lists")
        logger.info("test_check_shazam_songs_list_similarities completed successfully")