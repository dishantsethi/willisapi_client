import requests
import time
import json
import random

from willisapi_client.services.exceptions import UnableToLoginClientError

class AuthUtils:
    @staticmethod
    def login(url, data, headers, try_number):
        try:
            response = requests.post(url, json=data, headers=headers)
            res_json = response.json()
        except (requests.exceptions.ConnectionError, json.decoder.JSONDecodeError) as ex:
            if try_number == 3:
                raise UnableToLoginClientError
            time.sleep(random.random()*2)
            return AuthUtils.login(url, data, headers, try_number=try_number+1)
        else:
            return res_json
