from flask import Flask, jsonify
from flask_pydantic_spec import FlaskPydanticSpec, Request, Response
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date

app = Flask(__name__)
spec = FlaskPydanticSpec('flask', title='AutoTech API')
spec.register(app)

# Simulação de banco de dados
clientes = []
veiculos = []
ordens_de_servico = []
if __name__ == '__main__':
    app.run(debug=True)
