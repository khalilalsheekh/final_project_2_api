from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider


class APIChartList:
    config = ConfigProvider.load_from_file()
    basic_url = config['basic_url']
    chart_list_endpoint = config['endpoints']['chart_list_endpoint']

    def __init__(self, request: APIWrapper):
        self._request = request

    def get_chart_list(self):
        url = f"{self.basic_url}{self.chart_list_endpoint}"
        return self._request.get_request(url, headers=self.config["headers"])
