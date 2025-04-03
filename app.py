from flask import Flask, jsonify, request
from flask_openapi_spec import FlaskApiSpec
from flask_openapi_spec import Response, Request
from marshmallow import Schema, fields
from typing import List

app = Flask(__name__)


# Modelos para validação de dados
class Cliente(Schema):
    id = fields.Int(dump_only=True)  # Somente leitura
    nome = fields.Str(required=True)
    email = fields.Email(required=True)


class Veiculo(Schema):
    id = fields.Int(dump_only=True)
    cliente_id = fields.Int(required=True)
    modelo = fields.Str(required=True)
    ano = fields.Int(required=True)


class OrdemServico(Schema):
    id = fields.Int(dump_only=True)
    veiculo_id = fields.Int(required=True)
    descricao = fields.Str(required=True)
    status = fields.Str(required=True)


# Dados em memória (simulação de um banco de dados)
clientes = []
veiculos = []
ordens_de_servico = []

# Configuração da documentação
app.config.update({
    'APISPEC_SPEC': 'Flask',
    'APISPEC_SWAGGER_UI_URL': '/docs/',  # URL para acessar a documentação
    'APISPEC_SWAGGER_UI_VERSION': '3.25.0',
})

spec = FlaskApiSpec(app)  # Instância do FlaskApiSpec


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/clientes', methods=['GET'])
@spec.validate(resp=Response(HTTP_200=List[Cliente]), tags=["Clientes"])
def listar_clientes():

    return jsonify(clientes)


@app.route('/clientes', methods=['POST'])
@spec.validate(body=Request(Cliente), resp=Response(HTTP_201=Cliente), tags=["Clientes"])
def criar_cliente():

    body = request.json
    novo_cliente = body
    novo_cliente['id'] = len(clientes) + 1  # Gerar ID simples
    clientes.append(novo_cliente)
    return jsonify(novo_cliente), 201


@app.route('/veiculos', methods=['GET'])
@spec.validate(resp=Response(HTTP_200=List[Veiculo]), tags=["Veículos"])
def listar_veiculos():

    return jsonify(veiculos)


@app.route('/veiculos', methods=['POST'])
@spec.validate(body=Request(Veiculo), resp=Response(HTTP_201=Veiculo), tags=["Veículos"])
def criar_veiculo():

    body = request.json
    novo_veiculo = body
    novo_veiculo['id'] = len(veiculos) + 1
    veiculos.append(novo_veiculo)
    return jsonify(novo_veiculo), 201


@app.route('/os', methods=['GET'])
@spec.validate(resp=Response(HTTP_200=List[OrdemServico]), tags=["Ordens de Serviço"])
def listar_ordens_de_servico():

    return jsonify(ordens_de_servico)


@app.route('/os', methods=['POST'])
@spec.validate(body=Request(OrdemServico), resp=Response(HTTP_201=OrdemServico), tags=["Ordens de Serviço"])
def criar_ordem_servico():

    body = request.json
    nova_os = body
    nova_os['id'] = len(ordens_de_servico) + 1  # Gerar ID simples
    ordens_de_servico.append(nova_os)
    return jsonify(nova_os), 201


# Associando as rotas à documentação
spec.register(listar_clientes)
spec.register(criar_cliente)
spec.register(listar_veiculos)
spec.register(criar_veiculo)
spec.register(listar_ordens_de_servico)
spec.register(criar_ordem_servico)

# Esse if deve ser mantido no final
if __name__ == '__main__':
    app.run(debug=True)
