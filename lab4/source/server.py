from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/num1=<num1>&num2=<num2>")
def default(num1, num2):
	numbers = [int(num1), int(num2)]
	return {"sum" : numbers[0] + numbers[1],
			"sub" : numbers[0] - numbers[1],
			"mul" : numbers[0] * numbers[1],
			"div" : numbers[0] / numbers[1],
			"mod" : numbers[0] % numbers[1]}


if __name__ == "__main__":
	app.run(debug=True)
