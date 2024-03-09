from src.models.configs.base import Base
from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class Vendedor(Base):
    __tablename__ = "sistema_vendedor"
    __table_args__ = {'schema': 'dbo'}  # Especificando o esquema

    cod_id_vendedor = Column(Integer, primary_key=True, autoincrement=True)
    nom_vendedor = Column(String, nullable=False)  # nvarchar(MAX), sem limitação de tamanho definida
    des_email = Column(String, nullable=True)  # nvarchar(MAX), sem limitação de tamanho definida
    cod_loja = Column(Integer, ForeignKey('dbo.sistema_loja.cod_id_loja'), nullable=False)
    dat_criacao = Column(Date, nullable=True)
    dat_alteracao = Column(Date, nullable=True, onupdate=func.current_date())

    # Relacionamento com a tabela sistema_loja
    lojas = relationship("Loja", backref="vendedores", lazy='subquery')
    def __repr__(self):
            return f'Vendedor(cod_id_vendedor = {self.cod_id_vendedor}, nom_vendedor = {self.nom_vendedor}, des_email = {self.des_email}, dat_criacao = {self.dat_criacao}, dat_alteracao = {self.dat_alteracao})'