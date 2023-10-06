import requests
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

    def get(self, url: str):
        headers = {
            "Content-Type": "application/json",
        }
        response = self.requests.get(url, headers=headers)
        return response

    def post(self, url: str, post_data: Dict[str, T], token_required: bool = False):
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        self.__is_token_required(headers, token_required)
        response = self.requests.post(url, headers=headers, data=post_data)
        return response

    def patch(self, url: str, patch_data: Dict[str, T], token_required: bool = False):
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        self.__is_token_required(headers, token_required)
        response = self.requests.post(url, headers=headers, data=patch_data)
        return response

    def delete(self, url: str, token_required: bool = False):
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        self.__is_token_required(headers, token_required)
        response = self.requests.delete(url, headers=headers)
        return response
