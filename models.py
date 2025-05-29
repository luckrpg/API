from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine


DATABASE_URL = "sqlite:///meu_banco.db"
engine = create_engine(DATABASE_URL)


SessionFactory = sessionmaker(bind=engine)


Session = scoped_session(SessionFactory)


db = SQLAlchemy()
db.engin = engine
db.session = Session()



# Modelos
class Cliente(db.Model):
    __tablename__ = "clientes"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)

    veiculos = db.relationship('Veiculo', backref='cliente', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email
        }


class Veiculo(db.Model):
    __tablename__ = "veiculos"

    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    modelo = db.Column(db.String(100), nullable=False)
    ano = db.Column(db.Integer, nullable=False)

    ordens_de_servico = db.relationship('OrdemServico', backref='veiculo', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "cliente_id": self.cliente_id,
            "modelo": self.modelo,
            "ano": self.ano
        }


class OrdemServico(db.Model):
    __tablename__ = "ordens_de_servico"

    id = db.Column(db.Integer, primary_key=True)
    veiculo_id = db.Column(db.Integer, db.ForeignKey('veiculos.id'), nullable=False)
    descricao = db.Column(db.String(300), nullable=False)
    status = db.Column(db.String(50), nullable=False)



def adicionar_cliente(nome, email):
    try:
        cliente = Cliente(nome=nome, email=email)
        db.session.add(cliente)
        db.session.commit()
        print("Cliente adicionado com sucesso!")
    except Exception as e:
        db.session.rollback()
        print(f"Erro ao adicionar cliente: {e}")
    finally:
        db.session.remove()


def listar_clientes():
    try:
        clientes = db.session.query(Cliente).all()
        return [cliente.to_dict() for cliente in clientes]
    except Exception as e:
        print(f"Erro ao listar clientes: {e}")
    finally:
        db.session.remove()



db.Model.metadata.create_all(engine)
