import requests
from enum import Enum

class Fetch:
    @staticmethod
    def get(url: str, **kwargs) -> str:
        return requests.request("GET", url, **kwargs).text
    @staticmethod
    def post(url: str, **kwargs) -> str:
        return requests.request("POST", url, **kwargs).text