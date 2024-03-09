from src.models.configs.base import Base
from sqlalchemy import Column, String, Integer, DateTime, Float, Date
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class Cliente(Base):
    __tablename__ = "sistema_cliente"
    __table_args__ = {'schema': 'dbo'}  # Especificando o esquema

    cod_id_cliente = Column(Integer, primary_key=True, autoincrement=True)
    des_nome = Column(String(255), nullable=False)
    des_sobrenome = Column(String(255), nullable=False)
    vlr_poder_compra = Column(Float, nullable=True)
    vlr_saldo = Column(Float, nullable=True)
    des_email = Column(String(255), nullable=True)
    num_telefone = Column(String(20), nullable=True)
    dat_nascimento = Column(Date, nullable=True)
    dat_cadastro = Column(DateTime, default=func.getdate(), nullable=True)

    vendas = relationship("Venda", backref="vendas", lazy='subquery')
    
    def __repr__(self):
            return f'Cliente (cod_id_cliente = {self.cod_id_cliente}, des_nome = {self.des_nome}, des_sobrenome = {self.des_sobrenome}, vlr_poder_compra = {self.vlr_poder_compra}, vlr_saldo = {self.vlr_saldo}, des_email = {self.des_email}, num_telefone = {self.num_telefone}, dat_nascimento = {self.dat_nascimento}, dat_cadastro = {self.dat_cadastro})'
 