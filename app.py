from flask import Flask, jsonify, request
from models import Cliente, Veiculo, OrdemServico, clientes, veiculos, ordens_de_servico

app = Flask(__name__)


# Funções de validação manual
def validar_cliente(dados):
    erros = {}
    if not isinstance(dados.get("nome"), str) or not dados["nome"]:
        erros["nome"] = "Nome é obrigatório e deve ser uma string."
    if not isinstance(dados.get("email"), str) or "@" not in dados["email"]:
        erros["email"] = "Email é obrigatório e deve ser válido."
    return erros


def validar_veiculo(dados):
    erros = {}
    if not isinstance(dados.get("cliente_id"), int):
        erros["cliente_id"] = "cliente_id é obrigatório e deve ser um inteiro."
    if not isinstance(dados.get("modelo"), str) or not dados["modelo"]:
        erros["modelo"] = "Modelo é obrigatório e deve ser uma string."
    if not isinstance(dados.get("ano"), int):
        erros["ano"] = "Ano é obrigatório e deve ser um inteiro."
    return erros


def validar_ordem_servico(dados):
    erros = {}
    if not isinstance(dados.get("veiculo_id"), int):
        erros["veiculo_id"] = "veiculo_id é obrigatório e deve ser um inteiro."
    if not isinstance(dados.get("descricao"), str) or not dados["descricao"]:
        erros["descricao"] = "Descrição é obrigatória e deve ser uma string."
    if not isinstance(dados.get("status"), str) or not dados["status"]:
        erros["status"] = "Status é obrigatório e deve ser uma string."
    return erros


# Rotas
@app.route('/')
def hello_world():
    return "Hello, World!"


# Endpoints de Clientes
@app.route('/listar_clientes', methods=['GET'])
def listar_clientes():
    return jsonify([vars(c) for c in clientes])


@app.route('/cria_clientes', methods=['POST'])
def criar_cliente():
    dados = request.json
    erros = validar_cliente(dados)
    if erros:
        return jsonify({"erro": erros}), 400

    cliente = Cliente(nome=dados["nome"], email=dados["email"])
    clientes.append(cliente)
    return jsonify(vars(cliente)), 201


# Endpoints de Veículos
@app.route('/lista_veiculos', methods=['GET'])
def listar_veiculos():
    return jsonify([vars(v) for v in veiculos])


@app.route('/cria_veiculo', methods=['POST'])
def criar_veiculo():
    dados = request.json
    erros = validar_veiculo(dados)
    if erros:
        return jsonify({"erro": erros}), 400

    veiculo = Veiculo(cliente_id=dados["cliente_id"], modelo=dados["modelo"], ano=dados["ano"])
    veiculos.append(veiculo)
    return jsonify(vars(veiculo)), 201


# Endpoints de Ordens de Serviço
@app.route('/lista_servisos', methods=['GET'])
def listar_ordens_de_servico():
    return jsonify([vars(s) for s in ordens_de_servico])


@app.route('/cria_servos', methods=['POST'])
def criar_ordem_servico():
    dados = request.json
    erros = validar_ordem_servico(dados)
    if erros:
        return jsonify({"erro": erros}), 400

    ordem_servico = OrdemServico(veiculo_id=dados["veiculo_id"], descricao=dados["descricao"], status=dados["status"])
    ordens_de_servico.append(ordem_servico)
    return jsonify(vars(ordem_servico)), 201


# Main
if __name__ == '__main__':
    app.run(debug=True)
