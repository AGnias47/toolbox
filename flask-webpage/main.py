#!/usr/bin/python3
#
#   A. Gnias
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.3
#   Vim 8.0 [tabstop=3]

from flask import Flask
# contains the website
app = Flask(__name__)

# If the user goes to WEBPAGE/, run this
@app.route('/')
def hello_world():
	return "Welcome to the homepage!"

@app.route("/annika")
def annika():
	return "Annika is a dog!"

if __name__ == "__main__":
	app.run()
