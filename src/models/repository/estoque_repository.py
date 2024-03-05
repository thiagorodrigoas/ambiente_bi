from src.models.configs.connection import DBConnectionHandler
from src.models.entities.estoque import Estoque
from sqlalchemy.orm.exc import NoResultFound

class EstoqueRepository:
    def select(self):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Estoque).all()
                return data
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception

    def select_where(self, filters) -> Estoque:
        with DBConnectionHandler() as db:
            try:
                query = db.session.query(Estoque)
                for key, value in filters.items():
                    if hasattr(Estoque, key):
                        query = query.filter(getattr(Estoque, key) == value)
                estoque = query.first()
                if estoque == None:
                    raise NoResultFound
                else:
                    return estoque
            except NoResultFound:
                raise NoResultFound('Estoque Não encontrado!')
            except Exception as exception:
                db.session.rollback()
                raise exception

    def insert(self, estoque):
        with DBConnectionHandler() as db:
            try:
                data_isert = estoque
                db.session.add(data_isert)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def delete(self, cod_id_estoque):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Estoque).filter(Estoque.cod_id_estoque == cod_id_estoque).delete()
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
            
    def update(self, cod_id_estoque, estoque):
    #FIXME: corrigir o que será atualizado (estoque)
        with DBConnectionHandler() as db:
            try:
                db.session.query(Estoque).filter(Estoque.cod_id_estoque == cod_id_estoque).update({ "attrs_do_estoque": estoque })
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception