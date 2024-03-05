from src.models.configs.connection import DBConnectionHandler
from src.models.entities.loja import Loja
from sqlalchemy.orm.exc import NoResultFound

class LojaRepository:
    def select():
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Loja).all()
                return data
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception
            
    def select_where(self, filters) -> Loja:
        with DBConnectionHandler() as db:
            try:
                query = db.session.query(Loja)
                for key, value in filters.items():
                    if hasattr(Loja, key):
                        query = query.filter(getattr(Loja, key) == value)
                loja = query.first()
                if loja == None:
                    raise NoResultFound
                else:
                    return loja
            except NoResultFound:
                raise NoResultFound('Loja Não encontrado!')
            except Exception as exception:
                db.session.rollback()
                raise exception

    def insert(self,loja):
        with DBConnectionHandler() as db:
            try:
                data_isert = loja
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