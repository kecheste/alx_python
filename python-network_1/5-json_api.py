#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user with a given letter.
  - The letter is sent as the value of the variable `q`.
  - If no letter is provided, sends `q=""`.
"""
import sys
import requests


def search_user(letter):
    """ test"""
    url = f"http://0.0.0.0:5000/search_user"
    params = {"q": letter}
    try:
        response = requests.post(url, data=params)
        data = response.json()
        if data:
            print(f"[{data['id']}] {data['name']}")
        else:
            print("No result")
    except Exception as e:
        print("Not a valid JSON")


if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    search_user(letter)
