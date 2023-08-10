"""
Sends a request to a URL and displays the value of the X-Request-Id header in the response.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]  # URL received as the first command-line argument
    email = sys.argv[2]  # Email received as the second command-line argument

    payload = {"email": email}
    response = requests.post(url, data=payload)

    print("Your email is:", email)
    print(response.text)
