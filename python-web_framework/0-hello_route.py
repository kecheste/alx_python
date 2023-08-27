# /usr/bin/python3
from flask import Flask
# importing flask module into my app

app = Flask(__name__)

# Define a route for the root URL with strict_slashes=False


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'
# defining basic routing


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
# running the app
