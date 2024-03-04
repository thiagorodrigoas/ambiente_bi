from models.configs.connection import DBConnectionHandler
from models.entities.loja import Loja
from sqlalchemy.orm.exc import NoResultFound

class LojaRepository:
    def select(self):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Loja).all()
                return data
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception

    def insert(self,nom_loja, cod_long, cod_lat, des_bairro, des_pais, des_estado, des_tamanho_loja, dat_criacao, dat_alteracao):
        with DBConnectionHandler() as db:
            try:
                data_isert = Loja(nom_loja, cod_long, cod_lat, des_bairro, des_pais, des_estado, des_tamanho_loja, dat_criacao, dat_alteracao)
                db.session.add(data_isert)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def delete(self, cod_id_loja):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Loja).filter(Loja.cod_id_loja == cod_id_loja).delete()
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def update(self, cod_id_loja, loja):
    #FIXME: corrigir o que será atualizado (loja)
        with DBConnectionHandler() as db:
            try:
                db.session.query(Loja).filter(Loja.cod_id_loja == cod_id_loja).update({ "attrs_do_loja": loja })
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception