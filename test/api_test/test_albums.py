import unittest
import logging
from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider
from logic.api.api_albums import APIAlbums

logging.basicConfig(filename='../../test_api.log', level=logging.INFO)
logger = logging.getLogger(__name__)


class TestAlbums(unittest.TestCase):
    def setUp(self):
        self.api_request = APIAlbums(APIWrapper())
        self.config = ConfigProvider.load_from_file()
        logger.info("-" * 26)

    def tearDown(self):
        self.api_request = None
        logger.info("-" * 26)

    def test_check_albums_details_by_id_and_type(self):
        """
        Test the retrieval of album details.
        Verifies the response status, album ID, and type.
        """
        logger.info("Starting test_check_albums_details_by_id_and_type")
        querystring = self.config["query_strings"]["albums_details_query"]
        response = self.api_request.get_albums_details(querystring)
        self.assertTrue(response.ok)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data["data"][0]["id"], querystring["id"])
        self.assertEqual(response.data["data"][0]["type"], "albums")
        logger.info("test_check_albums_details_by_id_and_type completed successfully")
