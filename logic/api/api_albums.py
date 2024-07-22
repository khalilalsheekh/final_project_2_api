from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider


class APIAlbums:
    config = ConfigProvider.load_from_file()
    basic_url = config["basic_url"]
    albums_details_endpoint = config["endpoints"]["albums_details_endpoint"]

    def __init__(self, request: APIWrapper):
        self._request = request

    def get_albums_details(self, querystring):
        url = f"{self.basic_url}{self.albums_details_endpoint}"
        return self._request.get_request(url, headers=self.config["headers"], params=querystring)
