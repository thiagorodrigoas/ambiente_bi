from models.configs.connection import DBConnectionHandler
from models.entities.produto import Produto
from sqlalchemy.orm.exc import NoResultFound

class ProdutoRepository:
    def select(self):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Produto).all()
                return data
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception

    def insert(self, nom_produto, vlr_custo, des_produto, des_ticket_price, dat_criacao, dat_alteracao):
        with DBConnectionHandler() as db:
            try:
                data_isert = Produto(nom_produto, vlr_custo, des_produto, des_ticket_price, dat_criacao, dat_alteracao)
                db.session.add(data_isert)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def delete(self, cod_id_produto):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Produto).filter(Produto.cod_id_produto == cod_id_produto).delete()
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def update(self, cod_id_produto, produto):
    #FIXME: corrigir o que será atualizado (produto)
        with DBConnectionHandler() as db:
            try:
                db.session.query(Produto).filter(Produto.cod_id_produto == cod_id_produto).update({ "attrs_do_produto": produto })
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception