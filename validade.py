from flask import Flask, jsonify, render_template

from flask_pydantic_spec import FlaskPydanticSpec
import datetime
from datetime import datetime
from dateutil.relativedelta import relativedelta

app = Flask(__name__)


spec = FlaskPydanticSpec('flask',
                         title='First API - SENAI',
                         version='1.0.0')
spec.register(app)


@app.route('/valid')
def validado(ano, mes, dia):
    try:
        prazo = 12

        cadastro = datetime(int(ano)), int(mes), int(dia).date()

        meses = cadastro.today() + relativedelta(months=prazo)

        anos = cadastro.today() + relativedelta(years=prazo)

        semanas = cadastro.today() + relativedelta(week=prazo)

        dias = cadastro.today() + relativedelta(days=prazo)

        return jsonify({(f'"antes" - {abs(datetime.today().strftime("%d-%m-%Y"))}, '
                         f"cadastro - {cadastro}
                         f'"dias"- {dias}, '
                         f'"semanas"- {semanas}, '
                         f'"meses"- {meses},'
                         f'"anos"- {anos}')}
                       )


if __name__ == '__main__':
    app.run(debug=True)
