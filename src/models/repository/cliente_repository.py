from src.models.configs.connection import DBConnectionHandler
from src.models.entities.cliente import Cliente
from sqlalchemy.orm.exc import NoResultFound

class ClienteRepository:
    def __init__(self) -> None:
        pass
    
    def select(self):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Cliente).all()
                return data
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception

    def insert(self, cliente):
        with DBConnectionHandler() as db:
            try:
                data_isert = cliente
                db.session.add(data_isert)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def delete(self, cod_id_cliente):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Cliente).filter(Cliente.cod_id_cliente == cod_id_cliente).delete()
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def update(self, cod_id_cliente, cliente):
    #FIXME: corrigir o que será atualizado (cliente)
        with DBConnectionHandler() as db:
            try:
                db.session.query(Cliente).filter(Cliente.cod_id_cliente == cod_id_cliente).update({ "attrs_do_cliente": cliente })
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception