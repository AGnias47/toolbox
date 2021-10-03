#!/usr/bin/python3
#
#   A. Gnias
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.3
#   Vim 8.0 [tabstop=3]

from flask import Flask, jsonify
# contains the website
app = Flask(__name__)

def read_payload(fname):
	with open(fname, 'r') as F:
		content = F.read()
	return content

@app.route('/')
def hello_world():
	return "Welcome to the homepage!"

@app.route("/annika")
def annika():
	return "Annika is a dog!"

@app.route("/api/v1/lorem", methods=["GET"])
def api_lorem():
	return read_payload("api_sample_content/lorem")
	

if __name__ == "__main__":
	app.run()
