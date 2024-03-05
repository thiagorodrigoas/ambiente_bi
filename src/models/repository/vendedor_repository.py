from src.models.configs.connection import DBConnectionHandler
from src.models.entities.vendedor import Vendedor
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


    def select_where(self, filters) -> Vendedor:
        with DBConnectionHandler() as db:
            try:
                query = db.session.query(Vendedor)
                for key, value in filters.items():
                    if hasattr(Vendedor, key):
                        query = query.filter(getattr(Vendedor, key) == value)
                vendedor = query.first()
                if vendedor == None:
                    raise NoResultFound
                else:
                    return vendedor
            except NoResultFound:
                raise NoResultFound('Vendedor Não encontrado!')
            except Exception as exception:
                db.session.rollback()
                raise exception


    def insert(self, vendedor):
        with DBConnectionHandler() as db:
            try:
                data_insert = vendedor
                db.session.add(data_insert)
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