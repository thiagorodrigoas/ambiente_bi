from src.models.configs.base import Base
from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship


class ItemVenda(Base):
    __tablename__ = "sistema_item_venda"
    __table_args__ = {'schema': 'dbo'}  # Especificando o esquema

    cod_id_item_venda = Column(Integer, primary_key=True, autoincrement=True)
    cod_venda = Column(Integer,  ForeignKey('dbo.sistema_venda.cod_id_venda'))  # nvarchar(MAX), sem limitação de tamanho definida
    #FIXME: COLOCAR ESSA COLUNA COMO FOREINHEY NO MODELO DE RELACIONAMENTO DE DADOS
    cod_produto = Column(Integer,  ForeignKey('dbo.sistema_produto.cod_id_produto'))  # nvarchar(MAX), sem limitação de tamanho definida
    qtd_produto = Column(Integer, nullable=True)  # nvarchar(MAX), sem limitação de tamanho definida
    vlr_preco = Column(Float, nullable=True)  # nvarchar(MAX), sem limitação de tamanho definida
    
    vendas = relationship("Venda", backref="item_vendas", lazy='subquery')
    produtos = relationship("Produtos", backref="item_vendas", lazy='subquery')
    
    def __repr__(self):
        return f'ItemVenda(cod_id_item_venda = {self.cod_id_item_venda}, cod_venda = {self.cod_venda}, cod_produto = {self.cod_produto}, qtd_produto = {self.qtd_produto}, vlr_preco = {self.vlr_preco})'