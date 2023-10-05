import requests
from api.urls.api_urls import ApiUrls
from typing import Dict, TypeVar
from dotenv import load_dotenv
import os

load_dotenv()
T = TypeVar("T")


class ApiRequests:

    def __init__(self):
        self.requests = requests.Session()

    def __is_token_required(self, headers: Dict[str, T], token_required: bool):
        if token_required:
            headers["Authorization"] = f"Bearer {os.getenv('GOREST_API_TOKEN')}"

    def get(self, url: ApiUrls):
        response = self.requests.get(url.value, headers={
            "Content-Type": "application-json"
        })
        return response

    def post(self, url: ApiUrls, post_data: Dict[str, T], token_required: bool = False):
        headers = {
            "Content-Type": "application-json"
        }
        self.__is_token_required(headers, token_required)
        response = self.requests.post(url.value, headers=headers, data=post_data)
        return response

    def patch(self, url: ApiUrls, patch_data: Dict[str, T], token_required: bool = False):
        headers = {
            "Content-Type": "application-json"
        }
        self.__is_token_required(headers, token_required)
        response = self.requests.post(url.value, headers=headers, data=patch_data)
        return response

    def delete(self, url: ApiUrls, token_required: bool = False):
        headers = {
            "Content-Type": "application-json"
        }
        self.__is_token_required(headers, token_required)
        response = self.requests.delete(url.value, headers=headers)
        return response
