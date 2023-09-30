import sys
import requests


id = sys.argv[1]

r = requests.get('https://jsonplaceholder.typicode.com/users/' + id + '/todos')
