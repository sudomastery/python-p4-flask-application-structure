#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# Basic routes so the app serves visible content
@app.route('/')
def index():
	return '<h1>Welcome to my page!</h1>'

@app.route('/<string:username>')
def user(username):
	return f'<h1>Profile for {username}</h1>'


if __name__ == '__main__':
	# Run as a script: python server/app.py
	app.run(port=5555, debug=True)
