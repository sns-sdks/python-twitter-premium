"""
    Main api entry
"""
import logging
from typing import Optional

import httpx

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
    def generate_bearer_token(consumer_key: str, consumer_secret: str):
        """
        Obtain bearer token by consumer credentials
        :param consumer_key:
        :param consumer_secret:
        :return:
        """
        data = {
            "grant_type": "client_credentials",
        }

        resp = httpx.post(
            url="https://api.twitter.com/oauth2/token",
            data=data,
            auth=(consumer_key, consumer_secret),
        )
        if resp.status_code >= 400:
            logger.error(resp.text)
            resp.raise_for_status()

        return resp.json()

    @staticmethod
    def invalidate_bearer_token(consumer_key: str, consumer_secret: str, access_token: str):
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
        resp = httpx.post(
            url="https://api.twitter.com/oauth2/invalidate_token",
            data=data,
            auth=(consumer_key, consumer_secret)
        )
        if resp.status_code >= 400:
            logger.error(resp.text)
            resp.raise_for_status()

        return resp.json()

    def _request(self):
        pass
