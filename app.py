from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/<name>')
def hello_name(name):
    return f'ola, {name}!'

@app.route('/soma/<num1>+<num2>')
def soma(num1, num2):
    return f'ola, {num1} + {num2} = {num1 + num2}'

@app.route('/somas/<int:num1>/<int:num2>')
def somas(num1, num2):
    return f'ola, {num1} + {num2} = {num1 + num2}'

if __name__ == '__main__':
    app.run(debug=True)