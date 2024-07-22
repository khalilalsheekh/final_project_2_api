from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider


class APIShazamSongs:
    config = ConfigProvider.load_from_file()
    basic_url = config["basic_url"]
    shazam_songs_details = config["endpoints"]["shazam_songs_details_endpoint"]
    shazam_songs_list_similarities_endpoint = config["endpoints"]["shazam_songs_list_similarities_endpoint"]

    def __init__(self, request: APIWrapper):
        self._request = request

    def get_shazam_songs_details(self, querystring):
        url = f"{self.basic_url}{self.shazam_songs_details}"
        return self._request.get_request(url, headers=self.config["headers"], params=querystring)

    def get_shazam_songs_list_similarities(self,querystring):
        url = f"{self.basic_url}{self.shazam_songs_list_similarities_endpoint}"
        return self._request.get_request(url, headers=self.config["headers"], params=querystring)
