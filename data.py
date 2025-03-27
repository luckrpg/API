from datetime import datetime, date
from flask import Flask, jsonify
from flask_pydantic_spec import FlaskPydanticSpec

app = Flask(__name__)
spec = FlaskPydanticSpec('flask',
                          title = 'First API - Senai',
                          version = '1.0.0',)
spec.register(app)
tempo = datetime.now()

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/<dia>/<mes>/<ano>')
def data(dia, mes, ano):

    try:
        dia = int(dia)
        mes = int(mes)
        ano = int(ano)
        temporecebido = datetime(ano, mes, dia)
        data_atual = datetime.now()
        data_composta = data_atual.strftime('%d/%m/%Y')

        if temporecebido > data_atual:
            situacao = 'futuro'
        elif temporecebido < data_atual:
            situacao = 'passado'
        else:
            situacao = 'presente'

        dias_diferenca = abs(temporecebido - data_atual).days
        meses_diferenca = dias_diferenca // 30
        anos_diferenca = dias_diferenca // 365.25

        return jsonify({'situacao': situacao,
                        "dias de diferenca": dias_diferenca,
                        "meses de diferenca": meses_diferenca,
                        "anos de diferenca": anos_diferenca})
    except TypeError:
        return jsonify({'situacao': 'erro'})


if __name__ == '__main__':
    app.run(debug=True)