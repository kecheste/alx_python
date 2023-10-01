import csv
import requests
import sys


id = sys.argv[1]

r = requests.get('https://jsonplaceholder.typicode.com/users/' + id)
r2 = requests.get('https://jsonplaceholder.typicode.com/users/' + id + '/todos')
data = r.json()
data2 = r2.json()

data.get('username')

filename = data.get('id')
with open("{}.csv".format(filename), 'w', newline='') as file:
    writer = csv.writer(file)

    for item in data2:
        writer.writerow(["{},".format(data.get('id'))+"{},".format(data.get('username'))+"{},".format(item.get('completed'))+"{}".format(item.get('title'))])