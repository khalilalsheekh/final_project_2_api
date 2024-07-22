import unittest


from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider
from logic.api.api_events import APIEvents


class TestApiEvents(unittest.TestCase):
    def setUp(self):
        self.api_request = APIEvents(APIWrapper())
        self.config = ConfigProvider.load_from_file()

    def test_check_events(self):
        querystring = self.config["query_strings"]["events_query"]
        response = self.api_request.get_events(querystring)
        print(response.data)
        self.assertTrue(response.ok)
        self.assertEqual(response.status, 200)
        self.assertTrue(self.api_request.check_event_data_id(response.data, "599fee98-efb2-4047-8bb6-232f9b905f45"))
