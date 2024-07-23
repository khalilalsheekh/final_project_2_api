import unittest
import logging
from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider
from logic.api.api_search import APISearch

logging.basicConfig(filename='../../test_api.log', level=logging.INFO)
logger = logging.getLogger(__name__)


class TestApiSearch(unittest.TestCase):
    def setUp(self):
        self.api_request = APISearch(APIWrapper())
        self.config = ConfigProvider.load_from_file()
        logger.info("-" * 26)

    def tearDown(self):
        self.api_request = None
        logger.info("-" * 26)

    def test_check_search(self):
        """
        Test the search functionality.
        Verifies the response status and details of the first search result.
        """
        # Arrange
        logger.info("Starting test_check_search")
        querystring = self.config['query_strings']['search_query']

        # Act
        response = self.api_request.get_search(querystring)

        # Assert
        self.assertTrue(response.ok)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data["tracks"]["hits"][0]["track"]["subtitle"], "Billie Myers")
        self.assertEqual(response.data["tracks"]["hits"][0]["track"]["title"], "Kiss the Rain")
        logger.info("test_check_search completed successfully")

