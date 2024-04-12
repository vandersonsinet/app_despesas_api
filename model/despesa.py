from sqlalchemy import Column, String, Integer, DateTime, Float
from datetime import datetime
from typing import Union

from  model import Base

class Despesa(Base):
    __tablename__ = 'despesa'

    id = Column("pk_despesa", Integer, primary_key=True)
    descricao = Column(String(140), unique=True)
    quantidade = Column(Integer)
    valor = Column(Float)
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, descricao:str, quantidade:int, valor:float,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria uma Despesa

        Arguments:
            descricao: descrição da despesa.
            quantidade: quantidade da despesa a ser inserida no banco
            valor: valor da despesa
            data_insercao: data de quando a despesa foi inserida
        """
        self.descricao = descricao
        self.quantidade = quantidade
        self.valor = valor

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao


