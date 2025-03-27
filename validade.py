from flask import Flask, jsonify
from flask_pydantic_spec import FlaskPydanticSpec
from datetime import date
from dateutil.relativedelta import relativedelta


app = Flask(__name__)

spec = FlaskPydanticSpec('Flask',
                         title='Flask API',
                         version='1.0.0')
spec.register(app)

@app.route('/<quantidade>/<tipo>')
def validade(quanti, tip):

    try:
        data_atual_do_produto = date.today()
        quanti = int(quanti)
        que_pode_mudar = data_atual_do_produto

        if tip in ['ano', 'anos', 'year', 'years']:

            que_pode_mudar = data_atual_do_produto + relativedelta(years=quanti)
        elif tip in ['mes', 'meses', 'month', 'months']:

            que_pode_mudar = data_atual_do_produto + relativedelta(months=quanti)
        elif tip in ['dia', 'dias', 'day', 'days']:

            que_pode_mudar = data_atual_do_produto + relativedelta(days=quanti)
        else:
            return jsonify({'erro': 'isso não funcionou lol kkkkkkkkk'}), 400

        return jsonify({'data de validade é essa ai ->': que_pode_mudar.strftime('%d/%m/%Y')})


    except ValueError:
        return jsonify({'deu n =(': "error"}, 400)
    except TypeError:
        return jsonify({'deu n =(': "error"}, 400)


if __name__ == '__main__':
    app.run(debug=True)