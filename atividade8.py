from database import db


class Cliente(db.Model):
    __tablename__ = 'clientes'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    telefone = db.Column(db.String(15))
    endereco = db.Column(db.String(255))

    veiculos = db.relationship('Veiculo', backref='cliente', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Cliente {self.nome}>"

    cliente_bp = Blueprint('clientes', __name__)

    @cliente_bp.route('/clientes', methods=['POST'])
    def criar_cliente():
        data = request.get_json()
        try:
            cliente = Cliente(
                nome=data['nome'],
                cpf=data['cpf'],
                telefone=data.get('telefone', ''),
                endereco=data.get('endereco', '')
            )
            db.session.add(cliente)
            db.session.commit()
            return jsonify({'message': 'Cliente criado com sucesso!', 'cliente': {
                'id': cliente.id,
                'nome': cliente.nome,
                'cpf': cliente.cpf
            }}), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400