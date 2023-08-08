"""
Sends a request to a URL and displays the value of the X-Request-Id header in the response.
"""

import requests
import sys


def fetch_x_request_id(url):
    """
    Fetches the value of the X-Request-Id header in the response to a given URL.

    Args:
        url (str): The URL to send the request to.

    Returns:
        str: The value of the X-Request-Id header, or None if the header is not present.
    """
    response = requests.get(url)
    x_request_id = response.headers.get("X-Request-Id")
    return x_request_id


if __name__ == "__main__":
    url = sys.argv[1]
    x_request_id = fetch_x_request_id(url)
    print(x_request_id)
