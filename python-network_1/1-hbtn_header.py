"""
Sends a request to a URL and displays the value of the X-Request-Id header in the response.
"""
import requests
import sys


def get_x_request_id(url):
    """Gets the value of the X-Request-Id header from the response to the given URL."""
    response = requests.get(str(url))
    return response.headers['X-Request-Id']


if __name__ == '__main__':
    url = sys.argv[1]
    print(get_x_request_id(url))
