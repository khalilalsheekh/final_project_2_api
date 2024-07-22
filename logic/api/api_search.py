from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider


class APISearch:
    config = ConfigProvider.load_from_file()
    basic_url = config['basic_url']
    search_endpoint = config['endpoints']['search_endpoint']

    def __init__(self, request: APIWrapper):
        self._request = request

    def get_search(self, querystring):
        url = f"{self.basic_url}{self.search_endpoint}"
        return self._request.get_request(url, headers=self.config["headers"], params=querystring)

