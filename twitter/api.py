"""
    Main api entry
"""
import json
import logging
import random
import string
import time
from typing import Optional
from urllib.parse import urlparse, quote_plus

import httpx

import twitter.models as models

logger = logging.getLogger(__name__)


class Api:
    """

    """
    BASE_URL = ""
    OAUTH_ENDPOINT = 'https://api.twitter.com/oauth2/token'

    def __init__(
            self,
            consumer_key: Optional[str] = None,
            consumer_secret: Optional[str] = None,
            access_token: Optional[str] = None,
            timeout=None,
            proxies=None,
    ):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self._timeout = timeout
        self.proxies = proxies
        self.session = httpx.Client()

    @staticmethod
    def generate_bearer_token(consumer_key: str, consumer_secret: str, *, return_json=False, **kwargs):
        """
        Obtain bearer token by consumer credentials
        :param consumer_key: The consumer api key.
        :param consumer_secret: The consumer api secret.
        :param return_json: If set with true, will return origin json data, or the instance for token.
        :param kwargs: Optional kwargs for httpx client.
        :return: Token data
        """
        data = {
            "grant_type": "client_credentials",
        }
        with httpx.Client(**kwargs) as client:
            resp = client.post(
                url="https://api.twitter.com/oauth2/token",
                data=data,
                auth=(consumer_key, consumer_secret),
            )
        if resp.status_code >= 400:
            logger.error(resp.text)
            resp.raise_for_status()
        if return_json:
            return

        return resp.json()

    @staticmethod
    def invalidate_bearer_token(consumer_key: str, consumer_secret: str, access_token: str, **kwargs):
        """
        To invalidate a bearer token.
        :param consumer_key:
        :param consumer_secret:
        :param access_token:
        :return:
        """
        data = {
            "access_token": access_token,
        }
        with httpx.Client(**kwargs) as client:
            resp = client.post(
                url="https://api.twitter.com/oauth2/invalidate_token",
                data=data,
                headers={
                    "Authorization": (
                        f'authorization: OAuth oauth_consumer_key="{consumer_key}", '
                        f'oauth_nonce="AUTO_GENERATED_NONCE", oauth_signature="AUTO_GENERATED_SIGNATURE",'
                        f'oauth_signature_method="HMAC-SHA1", oauth_timestamp="AUTO_GENERATED_TIMESTAMP", '
                        f'oauth_token="{access_token}", oauth_version="1.0"'
                    )
                }
            )
        if resp.status_code >= 400:
            logger.error(resp.text)
            resp.raise_for_status()

        return resp.json()

    def build_nonce(self):
        return ''.join(
            random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(32))

    def timestamp(self):
        return int(round(time.time()))

    def signatureBaseForRequest(self, url, params, method):
        param_string = ""
        sorted_keys = sorted(params.iterkeys())
        for key in sorted_keys:
            string = key + "=" + params[key]
            if param_string.__len__() > 0:
                param_string += "&" + string
            else:
                param_string = string
        params = quote_plus(param_string)

        url = urlparse(url)
        url = "https://api.twitter.com" + url.path
        url = quote_plus(url)

        method = method.upper()

        signature_base = method + "&" + url + "&" + params

        return signature_base

    def get_data(self, access_token, **kwargs):
        data = {"query": "TwitterDev", "maxResults": "100", "fromDate": "202006010000", "toDate": "202006100000"}

        with httpx.Client(**kwargs) as client:
            resp = client.post(
                url="https://api.twitter.com/1.1/tweets/search/30day/test.json",
                data=json.dumps(data),
                headers={
                    "Authorization": f"Bearer {access_token}"
                }
            )
        if resp.status_code >= 400:
            logger.error(resp.text)
            resp.raise_for_status()

        return resp.json()

    def _request(self):
        pass
