from flask import Flask, jsonify, render_template, redirect, url_for
from flask_pydantic_spec import FlaskPydanticSpec
from datetime import date
from dateutil.relativedelta import relativedelta

app = Flask(__name__)

spec = FlaskPydanticSpec('flask',
                         title='First API - SENAI',
                         version='1.0.0')
spec.register(app)


@app.route('/valid/<tipo>/<valor>', methods=['GET', 'POST'])
def verificar(tipo=None, valor=None):
    if tipo is None and valor is None:
        return jsonify({"error": "insira valores"
                        }), 400
    else:
        data_atual = date.today()
        tipos_validos = ['dia', 'week', 'mes', 'ano']
        try:
            if tipo in tipos_validos:
                valor = int(valor)
                data_validade = data_atual
                if tipo == 'dia':
                    data_validade = data_atual + relativedelta(days=valor)

                elif tipo == 'week':
                    data_validade = data_atual + relativedelta(weeks=valor)

                elif tipo == 'mes':
                    data_validade = data_atual + relativedelta(months=valor)

                elif tipo == 'ano':
                    data_validade = data_atual + relativedelta(years=valor)
                data_atual = data_atual.strftime('%d/%m/%Y')
                data_validade = data_validade.strftime('%d/%m/%Y')
                return jsonify({'data_atual': data_atual, 'valor': valor, 'data_validade': data_validade})
            else:
                raise TypeError
        except TypeError:
            return jsonify({'error': 'Erro de formato de data inserido'}), 400
        except ValueError:
            return jsonify({'error': 'Erro de valor inserido'}), 400


if __name__ == '__main__':
    app.run(debug=True)
