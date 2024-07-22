import requests

from infra.api.response_wrapper import ResponseWrapper


class APIWrapper:

    def __init__(self):
        self._request = None

    def get_request(self, url, params=None, body=None, headers=None, cookies=None, auth=None, json=None):
        try:
            response = requests.get(
                url,
                params=params,
                data=body,
                headers=headers,
                cookies=cookies,
                auth=auth,
                json=json
            )
            response.raise_for_status()
            return ResponseWrapper(ok=response.ok, status=response.status_code, data=response.json())
        except requests.exceptions.HTTPError as e:
            print(f'HTTP error occurred: {e}')
        except Exception as e:
            print(f'Other error occurred: {e}')
        return None

    def post_request(self, url, params=None, body=None, headers=None, cookies=None, auth=None, json=None):
        try:
            response = requests.post(
                url,
                params=params,
                data=body,
                headers=headers,
                cookies=cookies,
                auth=auth,
                json=json
            )
            response.raise_for_status()
            return ResponseWrapper(ok=response.ok, status=response.status_code, data=response.json())
        except requests.exceptions.HTTPError as e:
            print(f'HTTP error occurred: {e}')
        except Exception as e:
            print(f'Other error occurred: {e}')
        return None
