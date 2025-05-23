from flask import Flask, request, jsonify
from modells import Cliente, Veiculo, OrdemServico, init_db, db_session
from flask_pydantic_spec import FlaskPydanticSpec
from sqlalchemy import select

app = Flask(__name__)

spec = FlaskPydanticSpec(
    'flask',
    title='First API - SENAI',
    version='1.0.0')
spec.register(app)
init_db()

@app.route('/clientes', methods=['GET'])
def listar_clientes():
    try:
        clientes = db_session.execute(select(Cliente)).scalars().all()

        listar_cliente = []
        for cliente in clientes:
            listar_cliente.append(cliente.serialize())
        return jsonify({'clientes': listar_cliente})

    except Exception as e:
        return jsonify({'error': str(e)}), 500
@app.route('/cria_cliente', methods=['POST'])
def cria_cliente():
    data = request.get_json()
    cliente = Cliente(
        nome=data['nome'],
        cpf=data['cpf'],
        telefone=data['telefone'],
        endereco=data['endereco'],
    )
    cliente.save()
    return jsonify(cliente.serialize()), 201


@app.route('/clientes/atualiza', methods=['PUT'])
def atualiza_cliente(id):

    cliente = db_session.execute(select(Cliente).where(Cliente.id == id)).scalar_one_or_none()
    if not cliente:
        return jsonify({'message': 'Cliente não encontrado'}), 404

    data = request.get_json()
    cliente.nome = data.get('nome', cliente.nome)
    cliente.cpf = data.get('cpf', cliente.cpf)
    cliente.telefone = data.get('telefone', cliente.telefone)
    cliente.endereco = data.get('endereco', cliente.endereco)
    cliente.save()
    return jsonify(cliente.serialize())



@app.route('/veiculos', methods=['GET'])
def listar_veiculos():
    veiculos = db_session.execute(select(Veiculo)).scalars().all()
    return jsonify([v.serialize() for v in veiculos])



@app.route('/veiculos', methods=['POST'])
def cria_veiculo():
    data = request.json
    veiculo = Veiculo(
        cliente_id=data['cliente_id'],
        marca=data['marca'],
        modelo=data['modelo'],
        placa=data['placa'],
        ano_fabricacao=data['ano_fabricacao'],
    )
    veiculo.save()
    return jsonify(veiculo.serialize()), 201



@app.route('/veiculos/<int:id>', methods=['GET'])
def busca_veiculo(id):
    veiculo = db_session.execute(select(Veiculo).where(Veiculo.id == id)).scalar_one_or_none()
    if not veiculo:
        return jsonify({'message': 'Veículo não encontrado'}), 404
    return jsonify(veiculo.serialize())


@app.route('/veiculos/<int:id>', methods=['PUT'])
def atualiza_veiculo(id):
    veiculo = db_session.execute(select(Veiculo).where(Veiculo.id == id)).scalar_one_or_none()
    if not veiculo:
        return jsonify({'message': 'Veículo não encontrado'}), 404

    data = request.json
    # Corrected data.get usage
    veiculo.cliente_id = data.get('cliente_id', veiculo.cliente_id)
    veiculo.marca = data.get('marca', veiculo.marca)
    veiculo.modelo = data.get('modelo', veiculo.modelo)
    veiculo.placa = data.get('placa', veiculo.placa)
    veiculo.ano_fabricacao = data.get('ano_fabricacao', veiculo.ano_fabricacao)
    veiculo.save()
    return jsonify(veiculo.serialize())


@app.route('/ordens', methods=['GET'])
def listar_ordens():
    ordens = db_session.execute(select(OrdemServico)).scalars().all()
    return jsonify([o.serialize() for o in ordens])


@app.route('/ordens', methods=['POST'])
def cria_ordens():
    data = request.get_json()
    ordens = OrdemServico(
        veiculo_id=data['veiculo_id'],
        data_abertura=data['data_abertura'],
        descricao_servico=data['descricao_servico'],
        status=data['status'],
        valor_estimado=data['valor_estimado'],
    )
    ordens.save()
    return jsonify(ordens.serialize()), 201


@app.route('/ordens/<int:id>', methods=['GET'])
def busca_ordens(id):
    ordem = db_session.execute(select(OrdemServico).where(OrdemServico.id == id)).scalar_one_or_none()
    if not ordem:
        return jsonify({'message': 'Ordem de Serviço não encontrada'}), 404
    return jsonify(ordem.serialize())


@app.route('/ordens/<int:id>', methods=['PUT'])
def atualiza_ordens(id):
    ordem = db_session.execute(select(OrdemServico).where(OrdemServico.id == id)).scalar_one_or_none()
    if not ordem:
        return jsonify({'message': 'Ordem de Serviço não encontrada'}), 404

    data = request.json
    ordem.veiculo_id = data.get('veiculo_id', ordem.veiculo_id)
    ordem.data_abertura = data.get('data_abertura', ordem.data_abertura)
    ordem.descricao_servico = data.get('descricao_servico', ordem.descricao_servico)
    ordem.status = data.get('status', ordem.status)
    ordem.valor_estimado = data.get('valor_estimado', ordem.valor_estimado) # Corrected typo in variable name
    ordem.save()
    return jsonify(ordem.serialize())

if __name__ == '__main__':
    app.run(debug=True)