from src.models.configs.connection import DBConnectionHandler
from src.models.entities.venda import Venda
from sqlalchemy.orm.exc import NoResultFound

class VendaRepository:

    def select(self):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Venda).all()
                return data
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception


    def select_where(self, filters) -> Venda:
        with DBConnectionHandler() as db:
            try:
                query = db.session.query(Venda)
                for key, value in filters.items():
                    if hasattr(Venda, key):
                        query = query.filter(getattr(Venda, key) == value)
                venda = query.first()
                if venda == None:
                    raise NoResultFound
                else:
                    return venda
            except NoResultFound:
                raise NoResultFound('Vendedor Não encontrado!')
            except Exception as exception:
                db.session.rollback()
                raise exception


    def insert(self, venda):
        with DBConnectionHandler() as db:
            try:
                data_insert = venda
                db.session.add(data_insert)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def delete(self, cod_id_venda):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Venda).filter(Venda.cod_id_venda == cod_id_venda).delete()
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def update(self, cod_id_venda, venda):
    #FIXME: corrigir o que será atualizado (venda)
        with DBConnectionHandler() as db:
            try:
                db.session.query(Venda).filter(Venda.cod_id_vendedor == cod_id_venda).update({ "attrs_do_venda": venda })
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception