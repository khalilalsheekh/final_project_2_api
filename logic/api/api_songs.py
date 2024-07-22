from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider


class APISongs:
    config = ConfigProvider.load_from_file()
    basic_url = config["basic_url"]
    details_endpoint = config["endpoints"]["songs_details_endpoint"]
    events_endpoint = config['endpoints']['artists_endpoint']
    count_endpoint = config["endpoints"]["songs_count_endpoint"]
    specific_song_details_endpoint = config["endpoints"]["specific_song_details"]
    songs_v2_detect_endpoint = config["endpoints"]["songs_v2_detect_endpoint"]

    def __init__(self, request: APIWrapper):
        self._request = request

    def get_songs_details(self, querystring):
        url = f"{self.basic_url}{self.details_endpoint}"
        return self._request.get_request(url, headers=self.config["headers"], params=querystring)

    def get_related_artist(self, querystring):
        url = f"{self.basic_url}{self.events_endpoint}"
        return self._request.get_request(url, headers=self.config["headers"], params=querystring)

    def get_songs_count(self, querystring):
        url = f"{self.basic_url}{self.count_endpoint}"
        return self._request.get_request(url, headers=self.config["headers"], params=querystring)

    def get_specific_song_details(self, querystring):
        url = f"{self.basic_url}{self.specific_song_details_endpoint}"
        return self._request.get_request(url, headers=self.config["headers"], params=querystring)

    def post_songs_v2_detect(self, querystring, sound_data):
        url = f"{self.basic_url}{self.songs_v2_detect_endpoint}"
        return self._request.post_request(url, headers=self.config["songs_v2_detect_headers"], params=querystring,
                                          body=sound_data)

