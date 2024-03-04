from src.models.configs.base import Base
from sqlalchemy import Column, String, Integer, Float, Date
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class Produto(Base):
    __tablename__ = "sistema_produto"
    __table_args__ = {'schema': 'dbo'}  # Especificando o esquema

    cod_id_produto = Column(Integer, autoincrement=True, primary_key=True)
    nom_produto = Column(String, nullable=False)  # nvarchar(MAX)
    vlr_custo = Column(Float, nullable=True)
    des_produto = Column(String, nullable=True)  # nvarchar(MAX)
    des_ticket_price = Column(String, nullable=False)  # nvarchar(MAX)
    dat_criacao = Column(Date, nullable=True)
    dat_alteracao = Column(Date, nullable=True, onupdate=func.current_date())

    estoque = relationship("Estoque", back_populates="produto")

    def __repr__(self):
            return f'Produto(cod_id_produto = {self.cod_id_produto}, nom_produto = {self.nom_produto}, vlr_custo = {self.vlr_custo}, des_produto = {self.des_produto}, des_ticket_price = {self.des_ticket_price}, dat_criacao = {self.dat_criacao}, dat_alteracao = {self.dat_alteracao})'
 