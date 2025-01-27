import setuptools
import math


def get_client_version():
    try:
        cv = float(setuptools.version.metadata.version("willisapi_client"))
    except Exception as e:
        cv = 1.0
    return cv


class WillisapiClient:
    def __init__(self, *args, **kwargs) -> None:
        self.client_version = get_client_version()
        self.api_version = math.floor(self.client_version)
        self.api_uri = "api.brooklyn.health"
        self.env = kwargs["env"] if "env" in kwargs else None

    def get_base_url(self):
        if self.env:
            return f"https://{self.env}-{self.api_uri}/v{self.api_version}/"
        return f"https://{self.api_uri}/v{self.api_version}/"

    def get_login_url(self):
        return self.get_base_url() + "api-login"

    def get_upload_url(self):
        return self.get_base_url() + "api-upload"

    def get_download_url(self):
        return self.get_base_url() + "api-download"

    def get_diarize_remaining_calls_url(self):
        return self.get_base_url() + "api-willisdiarize-call-remaining"

    def get_diarize(self):
        return self.get_base_url() + "api-willisdiarize"

    def get_headers(self):
        return {"Content-Type": "application/json", "Accept": "application/json"}
