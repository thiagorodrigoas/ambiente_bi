from src.models.configs.base import Base
from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class Loja(Base):
    __tablename__ = "sistema_loja"
    __table_args__ = {'schema': 'dbo'}  # Especificando o esquema

    cod_id_loja = Column(Integer, primary_key=True, autoincrement=True)
    nom_loja = Column(String, nullable=False)  # nvarchar(MAX)
    cod_long = Column(String, nullable=True)  # nvarchar(MAX)
    cod_lat = Column(String, nullable=True)  # nvarchar(MAX)
    des_bairro = Column(String, nullable=True)  # nvarchar(MAX)
    des_pais = Column(String, nullable=True)  # nvarchar(MAX)
    des_estado = Column(String, nullable=True)  # nvarchar(MAX)
    des_tamanho_loja = Column(String, nullable=True)  # nvarchar(MAX)
    dat_criacao = Column(Date, nullable=True)
    dat_alteracao = Column(Date, nullable=True, onupdate=func.current_date())

    vendedores = relationship("Vendedor", back_populates="lojas")


    def __repr__(self):
            return f'Loja(cod_id_loja= {self.cod_id_loja}, nom_loja = {self.nom_loja}, cod_long = {self.cod_long}, cod_lat = {self.cod_lat}, des_bairro = {self.des_bairro}, des_pais = {self.des_pais}, des_estado = {self.des_estado}, des_tamanho_loja = {self.des_tamanho_loja}, dat_criacao = {self.dat_criacao}, dat_alteracao = {self.dat_alteracao})'