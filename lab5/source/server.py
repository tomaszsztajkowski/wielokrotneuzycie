from flask import Flask, request

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello, World!"

@app.route("/", methods=['POST'])
def math():
    content = request.get_json()
    # numbers = [int(num1), int(num2)
    print(content, type(content))
    if 'num1' in content and 'num2' in content:
        numbers = [int(content['num1']), int(content['num2'])]
    return {"sum" : numbers[0] + numbers[1],
            "sub" : numbers[0] - numbers[1],
            "mul" : numbers[0] * numbers[1],
            "div" : numbers[0] / numbers[1],
            "mod" : numbers[0] % numbers[1]}


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=4080)

