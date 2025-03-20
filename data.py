from flask import Flask, jsonify
import datetime
from datetime import datetime
app = Flask(__name__)

@app.route('/dia/')
def dia():
    agora = datetime.now()
    agora = agora.strftime('%Y-%m-%d | %H:%M:%S')
    return jsonify({"agora": agora}), 200
@app.route('/dia_atua/<data>')
def dias_valores(data):
        data_entrada = datetime.strptime(data, '%Y-%m-%d')
        data_atual = datetime.now()


        days_difference = abs((data_atual - data_entrada).days)


        years_difference = abs(data_atual.year - data_entrada.year)
        months_difference = abs(data_atual.month - data_entrada.month)

        total_months_difference = years_difference * 12 + months_difference

        return {
            "dias_de_differença": days_difference,
            "meses_de_diferença": total_months_difference}
if __name__ == '__main__':
    app.run(debug=True)