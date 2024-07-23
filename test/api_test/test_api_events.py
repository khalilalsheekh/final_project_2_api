import unittest
import logging
from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider
from logic.api.api_events import APIEvents

logging.basicConfig(filename='../../test_api.log', level=logging.INFO)
logger = logging.getLogger(__name__)


class TestApiEvents(unittest.TestCase):
    def setUp(self):
        self.api_request = APIEvents(APIWrapper())
        self.config = ConfigProvider.load_from_file()
        logger.info("-" * 26)

    def tearDown(self):
        self.api_request = None
        logger.info("-" * 26)

    def test_check_events(self):
        """
        Test the retrieval of events.
        Verifies the response status and the ID of the first event in the response.
        """
        # Arrange
        logger.info("Starting test_check_events")
        querystring = self.config["query_strings"]["events_query"]

        # Act
        response = self.api_request.get_events(querystring)

        # Assert
        self.assertTrue(response.ok)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data["data"][0]["id"], "599fee98-efb2-4047-8bb6-232f9b905f45")
        logger.info("test_check_events completed successfully")

