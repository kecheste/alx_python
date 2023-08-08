"""
Fetches the status from https://alu-intranet.hbtn.io/status
"""

import requests


def fetch_url(url):
    """
    Fetches the content of a given URL.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The content of the URL.

    Raises:
        requests.exceptions.RequestException: If an error occurs while making the request.
    """
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    body = fetch_url(url)
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body.decode("utf-8"))
