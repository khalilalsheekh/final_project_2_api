import unittest
import logging
from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider
from logic.api.api_chart_list import APIChartList

logging.basicConfig(filename='../../test_api.log', level=logging.INFO)
logger = logging.getLogger(__name__)


class TestApiChartList(unittest.TestCase):
    def setUp(self):
        self.api_request = APIChartList(APIWrapper())
        self.config = ConfigProvider.load_from_file()
        logger.info("-" * 26)

    def tearDown(self):
        self.api_request = None
        logger.info("-" * 26)

    def test_check_chart_list(self):
        """
        Test the retrieval of chart list.
        Verifies the response status and details of the first country in the list.
        """
        # Arrange
        logger.info("Starting test_check_chart_list")

        # Act
        response = self.api_request.get_chart_list()

        # Assert
        self.assertTrue(response.ok)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data["countries"][0]["id"], "DE")
        self.assertEqual(response.data["countries"][0]["name"], "Germany")
        logger.info("test_check_chart_list completed successfully")

