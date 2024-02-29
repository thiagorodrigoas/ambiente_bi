from infra.configs.connection import DBConnectionHandler
from infra.entities.vendedor import Vendedor
from sqlalchemy.orm.exc import NoResultFound

class VendedorRepository:

    def select(self):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Vendedor).all()
                return data
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception

    def insert(self,nom_vendedor, des_email, cod_loja, dat_criacao, dat_alteracao):
        with DBConnectionHandler() as db:
            try:
                data_isert = Vendedor(nom_vendedor, des_email, cod_loja, dat_criacao, dat_alteracao)
                db.session.add(data_isert)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def delete(self, cod_id_vendedor):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Vendedor).filter(Vendedor.cod_id_vendedor == cod_id_vendedor).delete()
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def update(self, cod_id_vendedor, vendedor):
    #FIXME: corrigir o que será atualizado (vendedor)
        with DBConnectionHandler() as db:
            try:
                db.session.query(Vendedor).filter(Vendedor.cod_id_vendedor == cod_id_vendedor).update({ "attrs_do_vendedor": vendedor })
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception