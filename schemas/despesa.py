from pydantic import BaseModel
from typing import Optional, List
from model.despesa import Despesa


class DespesaEditarSchema(BaseModel):
    """ Define como uma nova despesa a ser inserida deve ser representada
    """
    id: int
    descricao: str 
    quantidade: Optional[int]
    valor: float

class DespesaSchema(BaseModel):
    """ Define como uma nova despesa a ser inserida deve ser representada
    """
    descricao: str = "Despesa de Alimentação"
    quantidade: Optional[int] = 1
    valor: float = 75.00


class DespesaBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca que será
        feita apenas com base no nome da despesa.
    """
    nome: str = "Teste"

class ListagemDespesasSchema(BaseModel):
    """ Define como uma listagem de produtos será retornada.
    """
    produtos:List[DespesaSchema]


def apresenta_despesas(despesas: List[Despesa]):
    """ Retorna uma representação da despesa seguindo o schema definido em
        DespesaViewSchema.
    """
    result = []
    for despesa in despesas:
        result.append({
            "descricao": despesa.descricao,
            "quantidade": despesa.quantidade,
            "valor": despesa.valor,
            "id": despesa.id,
        })

    return {"despesas": result}


class DespesaViewSchema(BaseModel):
    """ Define como uma despesa será retornada: despesa.
    """
    id: int = 1
    nome: str = "Despesa de Deslocamento"
    quantidade: Optional[int] = 1
    valor: float = 50.00


class DespesaDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    id: str

def apresenta_despesa(despesa: Despesa):
    """ Retorna uma representação da despesa seguindo o schema definido em
        DespesaViewSchema.
    """
    return {
        "id": despesa.id,
        "nome": despesa.nome,
        "quantidade": despesa.quantidade,
        "valor": despesa.valor
    }
