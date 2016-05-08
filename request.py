from flask import Flask
from string_search import *
from flask import request
import pdb

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/search')
def search():
	return find_string(request.args.get("query"))

if __name__ == '__main__':
    app.run(debug=True)
