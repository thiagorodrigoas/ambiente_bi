from infra.configs.connection import DBConnectionHandler
from infra.entities.estoque import Estoque
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

    def insert(self, cod_loja, cod_produto, qtd_produto, dat_criacao, dat_alteracao):
        with DBConnectionHandler() as db:
            try:
                data_isert = Estoque(cod_loja, cod_produto, qtd_produto, dat_criacao, dat_alteracao)
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