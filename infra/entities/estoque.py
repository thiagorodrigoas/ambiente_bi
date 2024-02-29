from infra.configs.base import Base
from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class Estoque(Base):
    __tablename__ = "sistema_estoque"
    __table_args__ = {'schema': 'dbo'}  # Especificando o esquema

    cod_id_estoque = Column(Integer, primary_key=True)
    cod_loja = Column(Integer, nullable=True)
    cod_produto = Column(Integer, ForeignKey('dbo.sistema_produto.cod_id_produto'), nullable=True)
    qtd_produto = Column(Integer, nullable=True)
    dat_criacao = Column(Date, nullable=True)
    dat_alteracao = Column(Date, nullable=True, onupdate=func.current_date())

    # Definindo a relação com a tabela sistema_produto
    produto = relationship("Produto", back_populates="estoque")


    def __repr__(self):
            return f'Estoque(cod_id_estoque = {self.cod_id_estoque}, cod_loja = {self.cod_loja}, cod_produto = {self.cod_produto}, qtd_produto = {self.qtd_produto}, dat_criacao = {self.dat_criacao}, dat_alteracao = {self.dat_alteracao})'
    

# Adicionando a relação inversa na classe Produto
# Produto.estoque = relationship("Estoque", back_populates="produto")