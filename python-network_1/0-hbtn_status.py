"""
Fetches the status from https://alu-intranet.hbtn.io/status
"""

import requests


def fetch_url(url):
    """Fetches a given url
    arg = url
    returns response.text    
    """
    response = requests.get(url)
    return response.text


if __name__ == '__main__':
    url = 'https://alu-intranet.hbtn.io/status'
    body = fetch_url(url)
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
