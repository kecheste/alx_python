"""
Sends a request to a URL and displays the value of the X-Request-Id header in the response.
"""
import requests
import sys


def search_user(letter):
    """Sends a POST request to http://0.0.0.0:5000/search_user with the given letter."""
    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': letter}
    response = requests.post(url, data=data)

    if response.status_code == 200:
        response_json = response.json()
        if response_json:
            print('[{id}] {name}'.format(
                id=response_json['id'], name=response_json['name']))
        else:
            print('No result')
    else:
        if response.headers['Content-Type'] == 'application/json':
            print('Not a valid JSON')
        else:
            print('Error: {}'.format(response.status_code))


if __name__ == '__main__':
    letter = sys.argv[1] if len(sys.argv) > 1 else ''
    search_user(letter)
