from src.models.configs.base import Base
from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship


class Venda(Base):
    __tablename__ = "sistema_venda"
    __table_args__ = {'schema': 'dbo'}  # Especificando o esquema

    cod_id_venda = Column(Integer, primary_key=True, autoincrement=True)
    cod_vendedor = Column(Integer,  ForeignKey('dbo.sistema_vendedor.cod_id_vendedor'))  # nvarchar(MAX), sem limitação de tamanho definida
    cod_cliente = Column(Integer,  ForeignKey('dbo.sistema_cliente.cod_id_cliente'))  # nvarchar(MAX), sem limitação de tamanho definida
    dat_criacao = Column(Date, nullable=True)
    
    # Relacionamento com a tabela sistema_loja
    vendedores = relationship("Vendedor", backref="vendas", lazy='subquery')
    clientes = relationship("Cliente", backref="vendas", lazy='subquery')
    
    def __repr__(self):
        return f'Venda(cod_id_venda = {self.cod_id_venda}, cod_vendedor = {self.cod_vendedor}, cod_cliente = {self.cod_cliente}, dat_criacao = {self.dat_criacao})'