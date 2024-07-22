from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider


class APIArtists:
    config = ConfigProvider.load_from_file()
    basic_url = config["basic_url"]
    artists_details_endpoint = config["endpoints"]["artist_details_endpoint"]
    artists_top_songs_endpoint = config["endpoints"]["artists_top_songs_endpoint"]
    artists_latest_release_endpoint = config["endpoints"]["artists_latest_release_endpoint"]
    artists_summary_endpoint = config["endpoints"]["artists_summary_endpoint"]

    def __init__(self, request: APIWrapper):
        self._request = request

    def get_artists_details(self, querystring):
        url = f"{self.basic_url}{self.artists_details_endpoint}"
        return self._request.get_request(url, headers=self.config["headers"], params=querystring)

    def get_artists_top_songs(self, querystring):
        url = f"{self.basic_url}{self.artists_top_songs_endpoint}"
        return self._request.get_request(url, headers=self.config["headers"], params=querystring)

    def get_artists_latest_release(self, querystring):
        url = f"{self.basic_url}{self.artists_latest_release_endpoint}"
        return self._request.get_request(url, headers=self.config["headers"], params=querystring)

    def get_artists_summary(self, querystring):
        url = f"{self.basic_url}{self.artists_summary_endpoint}"
        return self._request.get_request(url, headers=self.config["headers"], params=querystring)
