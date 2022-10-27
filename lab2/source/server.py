from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def default():
	return "Hello World!"

@app.route("/cmd/time/")
def time():
	return datetime.now().strftime("%H:%M:%S")
	
@app.route("/cmd/rev/<string>")
def rev(string):
	return string[::-1]

if __name__ == "__main__":
	app.run(debug=True)
