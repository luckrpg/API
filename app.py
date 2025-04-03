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

@app.route('/menos/<int:num1>/<int:num2>')
def menos(num1, num2):
    return f'ola, {num1} - {num2} = {num1 - num2}'

@app.route('/menos/<int:num1>/<int:num2>')
def multplica(num1, num2):
    return f'ola, {num1} * {num2} = {num1 * num2}'

@app.route('/menos/<int:num1>/<int:num2>')
def divisao(num1, num2):
    return f'ola, {num1} / {num2} = {num1 / num2}'

@app.route('/par/<num1>')
def par(num1):
    try:
        num1 = float(num1)
        if num1 % 2 == 0:
            return f'numero {num1}  par'
        else:
            return f' numero {num1} impar'
    except ValueError:
        return jsonify({'erro': 'Formato incorreto'})






# esse if aqui em baixo não pode sair deste local tem que ser o último
if __name__ == '__main__':
    app.run(debug=True)
