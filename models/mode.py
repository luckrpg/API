from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class Cliente(BaseModel):
    id: int
    nome: str
    cpf: str = Field(..., regex=r'^\d{11}$', description="CPF deve ter 11 dígitos")
    telefone: Optional[str] = None
    endereco: Optional[str] = None


class Veiculo(BaseModel):
    id: int
    cliente_id: int
    marca: str
    modelo: str
    placa: str
    ano_fabricacao: int = Field(..., ge=1900, le=date.today().year, description="Ano de fabricação do veículo")


class OrdemServico(BaseModel):
    id: int
    veiculo_id: int
    data_abertura: date
    descricao: str
    status: str = Field(..., regex="^(pendente|em andamento|concluido)$")
    valor_estimado: Optional[float]
