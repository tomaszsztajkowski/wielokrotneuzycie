from flask import Flask, request

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello, World!"

@app.route("/", methods=['POST'])
def math():
    content = request.get_json()
    output = {}
    if 'num1' in content and 'num2' in content:
        numbers = [int(content['num1']), int(content['num2'])]
        output = {"sum" : numbers[0] + numbers[1],
            "sub" : numbers[0] - numbers[1],
            "mul" : numbers[0] * numbers[1],
            "div" : numbers[0] / numbers[1],
            "mod" : numbers[0] % numbers[1]}
    if 'str' in content:
        output["lowercase"] = int(sum(map(str.islower, content['str'])))
        output["uppercase"] = sum(1 for c in content['str'] if c.isupper())
        output["digits"] = sum(c.isdigit() for c in content['str'])
        output["special"] = len(content['str']) - sum(c.isalpha() for c in content['str']) - sum(c.isdigit() for c in content['str']) - sum(c.isspace() for c in content['str'])
                
    return output


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=4080)

