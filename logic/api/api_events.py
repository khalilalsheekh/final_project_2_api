from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider


class APIEvents:
    config = ConfigProvider.load_from_file()
    base_url = config['basic_url']
    events_endpoint = config['endpoints']['shazam_events_endpoint']

    def __init__(self, request: APIWrapper):
        self._request = request

    def get_events(self, querystring):
        url = f"{self.base_url}{self.events_endpoint}"
        return self._request.get_request(url, headers=self.config["headers"], params=querystring)
