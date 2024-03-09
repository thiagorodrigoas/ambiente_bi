from src.models.configs.connection import DBConnectionHandler
from src.models.entities.item_venda import ItemVenda
from sqlalchemy.orm.exc import NoResultFound

class ItemVendaRepository:

    def select(self):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(ItemVenda).all()
                return data
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception


    def select_where(self, filters) -> ItemVenda:
        with DBConnectionHandler() as db:
            try:
                query = db.session.query(ItemVenda)
                for key, value in filters.items():
                    if hasattr(ItemVenda, key):
                        query = query.filter(getattr(ItemVenda, key) == value)
                item_venda = query.first()
                if item_venda == None:
                    raise NoResultFound
                else:
                    return item_venda
            except NoResultFound:
                raise NoResultFound('Vendedor Não encontrado!')
            except Exception as exception:
                db.session.rollback()
                raise exception


    def insert(self, item_venda):
        with DBConnectionHandler() as db:
            try:
                data_insert = item_venda
                db.session.add(data_insert)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def delete(self, cod_id_item_venda):
        with DBConnectionHandler() as db:
            try:
                db.session.query(ItemVenda).filter(ItemVenda.cod_id_item_venda == cod_id_item_venda).delete()
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def update(self, cod_id_item_venda, item_venda):
    #FIXME: corrigir o que será atualizado (venda)
        with DBConnectionHandler() as db:
            try:
                db.session.query(ItemVenda).filter(ItemVenda.cod_id_item_venda == cod_id_item_venda).update({ "attrs_do_cod_id_item_venda": item_venda })
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception