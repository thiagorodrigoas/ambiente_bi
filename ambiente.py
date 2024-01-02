from relogio_virtual import RelogioVirtual
from get_price_tickers import fetch_monthly_data, global_db
from desc_produtos import produtos, df_produtos
from cria_fake import cria_cliente_fake, cria_loja_fake, cria_vendedor_fake, cria_estoque_fake
from conecta_banco import CONFIG_DB,conecta_banco,inicia_cursor
import pandas as pd
from random import randint, choice,random
from tinydb import Query,TinyDB
from pathlib import Path
import schedule
from datetime import datetime
import time
import warnings
from pandas.core.common import SettingWithCopyWarning
warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)


clock = RelogioVirtual(start_year=2023, start_month=1, start_day=1, factor_hour_per_sec=24) # a cada 1 sec passa 24hs
dir_path = Path("database")
database_price = TinyDB(dir_path / "database_price.json",indent=2)
query = Query()

def limpa_db_sistema():
    print('Limpando ambiente...')
    with conecta_banco(CONFIG_DB) as con:
        #CRIA LOJAS DE ACORDO COM A qtd_lojas
        with inicia_cursor(con) as cursor:
            cursor.execute('''
                            DROP TABLE db_sistema.dbo.sistema_item_venda;
                            DROP TABLE db_sistema.dbo.sistema_venda;
                            DROP TABLE db_sistema.dbo.sistema_cliente;
                            DROP TABLE db_sistema.dbo.sistema_vendedor;
                            DROP TABLE db_sistema.dbo.sistema_estoque;
                            DROP TABLE db_sistema.dbo.sistema_produto;
                            DROP TABLE db_sistema.dbo.sistema_loja;
                            ''')
            cursor.execute('''
                            CREATE TABLE db_sistema.dbo.sistema_loja (
                                cod_id_loja int IDENTITY(1,1) NOT NULL,
                                nom_loja nvarchar(MAX) COLLATE Latin1_General_CI_AS NOT NULL,
                                cod_long nvarchar(MAX) COLLATE Latin1_General_CI_AS NULL,
                                cod_lat nvarchar(MAX) COLLATE Latin1_General_CI_AS NULL,
                                des_bairro nvarchar(MAX) COLLATE Latin1_General_CI_AS NULL,
                                des_pais nvarchar(MAX) COLLATE Latin1_General_CI_AS NULL,
                                des_estado nvarchar(MAX) COLLATE Latin1_General_CI_AS NULL,
                                des_tamanho_loja nvarchar(MAX) COLLATE Latin1_General_CI_AS NULL,
                                dat_criacao date NULL,
                                dat_alteracao date NULL,
                                CONSTRAINT pk_loja PRIMARY KEY (cod_id_loja)
                            );
                                                    
                            CREATE TABLE db_sistema.dbo.sistema_produto (
                                cod_id_produto int IDENTITY(1,1) NOT NULL,
                                nom_produto nvarchar(MAX) COLLATE Latin1_General_CI_AS NOT NULL,
                                vlr_custo float NULL,
                                des_produto nvarchar(MAX) COLLATE Latin1_General_CI_AS NULL,
                                des_ticket_price nvarchar(MAX) COLLATE Latin1_General_CI_AS NOT NULL,
                                dat_criacao date NULL,
                                dat_alteracao date NULL,
                                CONSTRAINT pk_produto PRIMARY KEY (cod_id_produto)
                            );
                                                    
                            CREATE TABLE db_sistema.dbo.sistema_estoque (
                                cod_id_estoque int IDENTITY(1,1) NOT NULL,
                                cod_loja int NULL,
                                cod_produto int NULL,
                                qtd_produto int NULL,
                                dat_criacao date NULL,
                                dat_alteracao date NULL,
                                CONSTRAINT pk_estoque PRIMARY KEY (cod_id_estoque),
                                CONSTRAINT fk_produto_estoque FOREIGN KEY (cod_produto) REFERENCES db_sistema.dbo.sistema_produto(cod_id_produto)
                            );
                                                    
                            CREATE TABLE db_sistema.dbo.sistema_vendedor (
                                cod_id_vendedor int IDENTITY(1,1) NOT NULL,
                                nom_vendedor nvarchar(MAX) COLLATE Latin1_General_CI_AS NOT NULL,
                                des_email nvarchar(MAX) COLLATE Latin1_General_CI_AS NULL,
                                cod_loja int NOT NULL,
                                dat_criacao date NULL,
                                dat_alteracao date NULL,
                                CONSTRAINT pk_vendedor PRIMARY KEY (cod_id_vendedor),
                                CONSTRAINT fk_loja_vendedor FOREIGN KEY (cod_loja) REFERENCES db_sistema.dbo.sistema_loja(cod_id_loja)
                            );
                                                    
                            CREATE TABLE db_sistema.dbo.sistema_cliente (
                                cod_id_cliente int IDENTITY(1,1) NOT NULL,
                                des_nome varchar(255) COLLATE Latin1_General_CI_AS NOT NULL,
                                des_sobrenome varchar(255) COLLATE Latin1_General_CI_AS NOT NULL,
                                vlr_poder_compra float NULL,
                                vlr_saldo float NULL,
                                des_email nvarchar(255) COLLATE Latin1_General_CI_AS NULL,
                                num_telefone varchar(20) COLLATE Latin1_General_CI_AS NULL,
                                dat_nascimento date NULL,
                                dat_cadastro datetime DEFAULT getdate() NULL,
                                CONSTRAINT pk_cliente PRIMARY KEY (cod_id_cliente)
                            );
                                                    
                            CREATE TABLE db_sistema.dbo.sistema_venda (
                                cod_id_venda int IDENTITY(1,1) NOT NULL,
                                cod_vendedor int NULL,
                                cod_cliente int NULL,
                                dat_criacao date NULL,
                                CONSTRAINT pk_venda PRIMARY KEY (cod_id_venda),
                                CONSTRAINT fk_cliente_venda FOREIGN KEY (cod_cliente) REFERENCES db_sistema.dbo.sistema_cliente(cod_id_cliente),
                                CONSTRAINT fk_vendedor_venda FOREIGN KEY (cod_vendedor) REFERENCES db_sistema.dbo.sistema_vendedor(cod_id_vendedor)
                            );
                                                    
                            CREATE TABLE db_sistema.dbo.sistema_item_venda (
                                cod_id_item_venda int IDENTITY(1,1) NOT NULL,
                                cod_venda int NOT NULL,
                                cod_produto int NULL,
                                qtd_produto int NULL,
                                vlr_preco float NULL,
                                CONSTRAINT pk_item_venda PRIMARY KEY (cod_id_item_venda),
                                CONSTRAINT fk_venda_item_venda FOREIGN KEY (cod_venda) REFERENCES db_sistema.dbo.sistema_venda(cod_id_venda)
                            );
                            ''')

def cria_produtos():
    with conecta_banco(CONFIG_DB) as con:
        with inicia_cursor(con) as cursor:
            print('Criando produtos...')
            datas_start = clock.get_current_time().date()#.strftime('%Y-%m-%d')
            df_produtos['dat_criacao'] = datas_start
            df_produtos['dat_alteracao'] = datas_start
            print('Precificando produtos...')
            
            tickets_list = [tick[0] for tick in produtos]
            database_price = fetch_monthly_data(tickets_list,clock.get_current_time())

            price_now = database_price.search(query.Date == datas_start.strftime('%Y-%m-01'))[0]
            df_produtos['vlr_custo'] = df_produtos['des_ticket_price'].map(price_now)
            produtos_colunas = list(df_produtos.columns)
            

            insert_produtos = f'''INSERT INTO db_sistema.dbo.sistema_produto ({', '.join(produtos_colunas)})
                                VALUES ({', '.join(['?'] * len(produtos_colunas))});'''
            cursor.executemany(insert_produtos, df_produtos.values.tolist())

def inicia_ambiente(qtd_lojas=5, relogio_virtual=clock.get_current_time()):
    print('Iniciando ambiente...')
    global clock
    global database_price
    global query
    clock = relogio_virtual
    
    

    with conecta_banco(CONFIG_DB) as con:
        #CRIA LOJAS DE ACORDO COM A qtd_lojas
        with inicia_cursor(con) as cursor:
            print('Criando lojas...')
            lista_lojas = cria_loja_fake(qtd_lojas=qtd_lojas)
            df_lojas = pd.DataFrame(lista_lojas)
            lojas_colunas = list(df_lojas.columns)
            insert_lojas = f'''INSERT INTO db_sistema.dbo.sistema_loja ({', '.join(lojas_colunas)})
                                VALUES ({', '.join(['?'] * len(lojas_colunas))});'''
            cursor.executemany(insert_lojas, df_lojas.values.tolist())
        
        # CADASTRA TODOS OS PRODUTOS
        with inicia_cursor(con) as cursor:
            print('Criando produtos...')
            datas_start = clock.get_current_time().date()#.strftime('%Y-%m-%d')
            df_produtos['dat_criacao'] = datas_start
            df_produtos['dat_alteracao'] = datas_start
            print('Precificando produtos...')
            
            tickets_list = [tick[0] for tick in produtos]
            database_price = fetch_monthly_data(tickets_list,clock.get_current_time())

            price_now = database_price.search(query.Date == datas_start.strftime('%Y-%m-01'))[0]
            df_produtos['vlr_custo'] = df_produtos['des_ticket_price'].map(price_now)
            produtos_colunas = list(df_produtos.columns)
            

            insert_produtos = f'''INSERT INTO db_sistema.dbo.sistema_produto ({', '.join(produtos_colunas)})
                                VALUES ({', '.join(['?'] * len(produtos_colunas))});'''
            cursor.executemany(insert_produtos, df_produtos.values.tolist())
              
        # CADASTRA ESTOQUES DAS LOJAS OS PRODUTOS
        with inicia_cursor(con) as cursor:
            print('Enchendo estoques...')
            select_sistema_produto = 'select * from db_sistema.dbo.sistema_produto'
            df_sel_produtos = pd.read_sql(select_sistema_produto,con)

            select_sistema_loja = 'select * from db_sistema.dbo.sistema_loja'
            df_sel_lojas = pd.read_sql(select_sistema_loja,con)
    
            lista_estoques = cria_estoque_fake(df_sel_lojas,df_sel_produtos)
            df_estoques = pd.DataFrame(lista_estoques)
            estoques_colunas = list(df_estoques.columns)
            insert_lojas = f'''INSERT INTO db_sistema.dbo.sistema_estoque ({', '.join(estoques_colunas)})
                                VALUES ({', '.join(['?'] * len(estoques_colunas))});'''
            cursor.executemany(insert_lojas, df_estoques.values.tolist())
       
        # CADASTRA VENDEDOR NAS LOJAS
        with inicia_cursor(con) as cursor:
            print('Contratando Venderores...')
            select_sistema_loja = 'select * from db_sistema.dbo.sistema_loja'
            df_sel_lojas = pd.read_sql(select_sistema_loja,con)

            lista_vendedores = cria_vendedor_fake(df_sel_lojas)
            df_vendedores = pd.DataFrame(lista_vendedores)
            vendedores_colunas = list(df_vendedores.columns)
            insert_vendedores = f'''INSERT INTO db_sistema.dbo.sistema_vendedor ({', '.join(vendedores_colunas)})
                                VALUES ({', '.join(['?'] * len(vendedores_colunas))});'''
            cursor.executemany(insert_vendedores, df_vendedores.values.tolist())
       
        # CADASTRA ALGUNS CLIENTES ALEATÓRIOS
        with inicia_cursor(con) as cursor:
            print('Cadastrando clientes...')
            lista_clientes = cria_cliente_fake(randint(50,100),clock.get_current_time())      
            df_clientes = pd.DataFrame(lista_clientes)
            clientes_colunas = list(df_clientes.columns)
            insert_clientes = f'''INSERT INTO db_sistema.dbo.sistema_cliente ({', '.join(clientes_colunas)})
                                VALUES ({', '.join(['?'] * len(clientes_colunas))});'''
            cursor.executemany(insert_clientes, df_clientes.values.tolist())

def clock_cria_loja(clock = clock):
    '''Cria loja de acordo com o RelogioVirtual'''
    with conecta_banco(CONFIG_DB) as con:
    #CRIA LOJAS DE ACORDO COM A qtd_lojas
        with inicia_cursor(con) as cursor:
            print('Criando loja...')
            lista_lojas = cria_loja_fake(qtd_lojas=1, clock=clock)
            df_lojas = pd.DataFrame(lista_lojas)
            lojas_colunas = list(df_lojas.columns)
            insert_lojas = f'''INSERT INTO db_sistema.dbo.sistema_loja ({', '.join(lojas_colunas)})
                                VALUES ({', '.join(['?'] * len(lojas_colunas))});'''
            cursor.executemany(insert_lojas, df_lojas.values.tolist())

    #CRIA LOJAS DE ACORDO COM A qtd_lojas
        with inicia_cursor(con) as cursor:
            last_inserted = '''SELECT * from sistema_loja se where cod_id_loja = IDENT_CURRENT('sistema_loja');'''
            results = pd.read_sql(last_inserted,con)#.iloc[0].to_dict()

            return results

def clock_cria_estoque(loja):
    with conecta_banco(CONFIG_DB) as con:
        # CADASTRA ESTOQUES DAS LOJAS OS PRODUTOS
        with inicia_cursor(con) as cursor:
            print('Enchendo estoques...')
            select_sistema_produto = 'select * from db_sistema.dbo.sistema_produto'
            df_sel_produtos = pd.read_sql(select_sistema_produto,con)

            lista_estoques = cria_estoque_fake(loja,df_sel_produtos)
            df_estoques = pd.DataFrame(lista_estoques)
            estoques_colunas = list(df_estoques.columns)
            insert_lojas = f'''IF NOT EXISTS(SELECT 1 FROM db_sistema.dbo.sistema_estoque  WHERE cod_loja = {loja['cod_id_loja'].iloc[0]})
                                INSERT INTO db_sistema.dbo.sistema_estoque ({', '.join(estoques_colunas)})
                                VALUES ({', '.join(['?'] * len(estoques_colunas))});'''
            cursor.executemany(insert_lojas, df_estoques.values.tolist())
        
        with inicia_cursor(con) as cursor:
            
            list_cod_produto = list(df_estoques['cod_produto'].sort_values())
            dat_criacao_loja = loja['dat_criacao'].iloc[0]

            price_now = database_price.search(query.Date == dat_criacao_loja.strftime('%Y-%m-01'))[0]

            update_produtos = df_sel_produtos[ df_sel_produtos['cod_id_produto'].isin(list_cod_produto)]
            
            update_produtos['vlr_custo'] = df_produtos['des_ticket_price'].map(price_now)
            update_produtos['dat_alteracao'] = dat_criacao_loja
            cursor.executemany("UPDATE sistema_produto SET vlr_custo = ?, dat_alteracao = ? WHERE cod_id_produto = ?", update_produtos[['vlr_custo','dat_alteracao','cod_id_produto']].values.tolist())
 
def clock_cria_venderores(loja):
    with conecta_banco(CONFIG_DB) as con:
        # CADASTRA VENDEDOR NAS LOJAS
        with inicia_cursor(con) as cursor:
            print('Contratando Venderores...')
            select_sistema_loja = 'select * from db_sistema.dbo.sistema_loja'
            df_sel_lojas = pd.read_sql(select_sistema_loja,con)

            lista_vendedores = cria_vendedor_fake(loja)
            df_vendedores = pd.DataFrame(lista_vendedores)
            vendedores_colunas = list(df_vendedores.columns)
            insert_vendedores = f'''INSERT INTO db_sistema.dbo.sistema_vendedor ({', '.join(vendedores_colunas)})
                                VALUES ({', '.join(['?'] * len(vendedores_colunas))});'''
            cursor.executemany(insert_vendedores, df_vendedores.values.tolist())

def clock_cria_clientes(qtd_clientes = 1):
    qtd_clientes = randint(1,10)
    with conecta_banco(CONFIG_DB) as con:
        with inicia_cursor(con) as cursor:
            print(f'Cadastrando {qtd_clientes} clientes...')
            lista_clientes = cria_cliente_fake(qtd_clientes,clock.get_current_time())      
            df_clientes = pd.DataFrame(lista_clientes)
            clientes_colunas = list(df_clientes.columns)
            insert_clientes = f'''INSERT INTO db_sistema.dbo.sistema_cliente ({', '.join(clientes_colunas)})
                                VALUES ({', '.join(['?'] * len(clientes_colunas))});'''
            cursor.executemany(insert_clientes, df_clientes.values.tolist())

def clock_atualiza_saldo_clientes():
    with conecta_banco(CONFIG_DB) as con:
        #CRIA LOJAS DE ACORDO COM A qtd_lojas
        with inicia_cursor(con) as cursor:
            #seleciona um cliente aleatório
            update_saldo_cliente = 'update sistema_cliente set vlr_saldo = round(vlr_saldo + vlr_poder_compra, 2)'
            cursor.execute(update_saldo_cliente)

def clock_realiza_venda():
    
    with conecta_banco(CONFIG_DB) as con:
        #CRIA LOJAS DE ACORDO COM A qtd_lojas
            #seleciona um cliente aleatório
            select_sistema_cliente = 'select * from db_sistema.dbo.sistema_cliente'
            df_sel_clientes = pd.read_sql(select_sistema_cliente,con)
            cliente = dict(df_sel_clientes.sample(n=1).iloc[0])
            
            #seleciona um vendedor aleatório
            select_id_vendedores = 'select cod_id_vendedor from db_sistema.dbo.sistema_vendedor'
            df_sel_id_vendedores = pd.read_sql(select_id_vendedores,con)
            vendedor = dict(df_sel_id_vendedores.sample(n=1).iloc[0])

            #produtos que vendedor pode vender (estoque)
            select_estoque_vend = f'''SELECT
                                        sv.cod_id_vendedor,
                                        sv.nom_vendedor,
                                        se.cod_loja,
                                        se.cod_produto,
                                        se.qtd_produto,
                                        se.dat_criacao,
                                        se.dat_alteracao,
                                        sp.nom_produto,
                                        sp.vlr_custo
                                    from
                                        sistema_loja sl
                                    left join sistema_estoque se on
                                        sl.cod_id_loja = se.cod_loja
                                    left join sistema_produto sp on
                                        sp.cod_id_produto = se.cod_produto
                                    left join sistema_vendedor sv on
                                        sv.cod_loja = sl.cod_id_loja 
                                    where
                                        sv.cod_id_vendedor = {vendedor['cod_id_vendedor']}'''
            df_estoque_vend = pd.read_sql(select_estoque_vend,con)

    # Cria uma lista dos produtos disponíveis
    itens_comprados = {}
    produtos_disponiveis = list(df_estoque_vend['cod_produto'])
    saldo_atual = cliente['vlr_saldo']

    rand = 1 - random()
    vontade_compra = round( rand * saldo_atual, 2)

    while saldo_atual > vontade_compra and produtos_disponiveis:
        # Escolhe um produto aleatório
        produto = dict(df_estoque_vend[df_estoque_vend['cod_produto']==choice(produtos_disponiveis)].iloc[0])
        preco = produto['vlr_custo']
        estoque = produto['qtd_produto'] or 0 
        
        # Verifica quantos deste produto o cliente pode comprar, considerando saldo e estoque
        max_itens_por_saldo = int(saldo_atual / preco)
        max_itens_por_estoque = estoque
        
        max_itens = min(max_itens_por_saldo, max_itens_por_estoque)
        
        if max_itens == 0:
            # Se não pode comprar nem 1 item, remove da lista
            produtos_disponiveis.remove(produto['cod_produto'])
            continue
        
        # Escolhe uma quantidade aleatória para comprar, entre 1 e o máximo possível
        qtde_comprada = randint(1, max_itens)
        
        # Atualiza o saldo e estoque
        compra_total = round(qtde_comprada * preco,2)
        saldo_atual -= round(compra_total,2)
        estoque -= qtde_comprada
        
        # Adiciona ao registro de itens comprados
        if produto['cod_produto'] in itens_comprados.keys():
            itens_comprados.update({produto['cod_produto'] : {
                               'cod_produto': produto['cod_produto'],
                               'qtd_produto': itens_comprados[produto['cod_produto']]['qtd_produto'] + qtde_comprada ,
                               'vlr_preco': itens_comprados[produto['cod_produto']]['vlr_preco'] + compra_total
                                }})
        else:
            itens_comprados.update({produto['cod_produto'] : 
                               {'cod_produto': produto['cod_produto'],
                               'qtd_produto': qtde_comprada ,
                               'vlr_preco': compra_total
                                }})
    
    if itens_comprados:
        with conecta_banco(CONFIG_DB) as con:
            #CRIA LOJAS DE ACORDO COM A qtd_lojas
            with inicia_cursor(con) as cursor:   
                #TODO: FAZER OS UPDATES DE ESTOQUE COMPRA E  
                
                sql_insert_venda = 'INSERT INTO db_sistema.dbo.sistema_venda (cod_vendedor,cod_cliente,dat_criacao) values ({},{},\'{}\')'.format(vendedor['cod_id_vendedor'],cliente['cod_id_cliente'],clock.get_current_time().date()) 
                cursor.execute(sql_insert_venda)
                print('Vendedor {}, realiza venda para cliente {} no dia {}'.format(vendedor['cod_id_vendedor'],cliente['cod_id_cliente'],clock.get_current_time()))
                    
                sql_get_last_venda = "SELECT cod_id_venda from sistema_venda sv where cod_id_venda = IDENT_CURRENT('sistema_venda')"
                id_last_venda = pd.read_sql(sql_get_last_venda,con)['cod_id_venda'].iloc[0]
                insert_item_venda = f'''INSERT
                                            INTO
                                            sistema_item_venda
                                        (cod_venda,
                                        cod_produto,
                                        qtd_produto,
                                        vlr_preco)
                                        values (?,?,?,?)'''
                
                df_itens_comprados = pd.DataFrame(itens_comprados).T
                df_itens_comprados['id_last_venda'] = id_last_venda
                cursor.executemany(insert_item_venda, df_itens_comprados[['id_last_venda','cod_produto','qtd_produto','vlr_preco']].values.tolist())
                
                update_saldo_cliente = 'update sistema_cliente set vlr_saldo = {} where cod_id_cliente = {}'.format(saldo_atual,cliente['cod_id_cliente'])
                #print(update_saldo_cliente)
                cursor.execute(update_saldo_cliente)

                update_qtd_produto_estoque = 'update sistema_estoque set qtd_produto = {}, dat_alteracao = \'{}\' where cod_loja = {} and cod_produto = {}'.format(estoque or 0,clock.get_current_time().date(),produto['cod_loja'],produto['cod_produto'])
                #print(update_qtd_produto_estoque)
                cursor.execute(update_qtd_produto_estoque)

def clock_multipla_vendas():
    for _ in range(randint(5,10)):
        clock_realiza_venda()

def clock_atualiza_estoque():
    with conecta_banco(CONFIG_DB) as con:
        #CRIA LOJAS DE ACORDO COM A qtd_lojas
        with inicia_cursor(con) as cursor:
            #SE O ESTOQUE ESTÁ COM A METADE DA QUANTIDADE MINIMA ATUALIZA.
            #TODO: CORRIGIR O NUMERO RANDOMICO QUE ESTÁ PARA TODOS OS PRODUTOS DO ESTOQUE
            update_qtd_estoque = f'''UPDATE
                                        sistema_estoque
                                    SET
                                        qtd_produto = case
                                            when sl.des_tamanho_loja = 'GRANDE' and qtd_produto < 40 then qtd_produto + {randint(85,155)}
                                            when sl.des_tamanho_loja = 'MEDIA' and qtd_produto < 20 then qtd_produto + {randint(40,75)}
                                            when sl.des_tamanho_loja = 'PEQUENA' and qtd_produto < 5 then qtd_produto + {randint(10,35)}
                                            else qtd_produto
                                            END,
                                        dat_alteracao = \'{clock.get_current_time().date()}\'
                                        FROM
                                            sistema_loja sl
                                        INNER JOIN sistema_estoque se on
                                            sl.cod_id_loja = se.cod_loja'''
            cursor.execute(update_qtd_estoque)
            print('Comprando Estoque das lojas....')

def clock_atualiza_custo_produto():
    #TODO: atualizar mensalmente custo de produto baseado no tinydb
    with conecta_banco(CONFIG_DB) as con:
        # CADASTRA ESTOQUES DAS LOJAS OS PRODUTOS
        with inicia_cursor(con) as cursor:
            print('Atualizando custo de produtos...')
            select_sistema_produto = 'select * from db_sistema.dbo.sistema_produto'
            update_produtos = pd.read_sql(select_sistema_produto,con)

        with inicia_cursor(con) as cursor:
            #TODO: fazer update do custo dos produtos
            dat_atualizacao = clock.get_current_time().date()
            price_now = database_price.search(query.Date == dat_atualizacao.strftime('%Y-%m-01'))[0]
            
            update_produtos['vlr_custo'] = df_produtos['des_ticket_price'].map(price_now)
            update_produtos['dat_alteracao'] = dat_atualizacao
            cursor.executemany("UPDATE sistema_produto SET vlr_custo = ?, dat_alteracao = ? WHERE cod_id_produto = ?", update_produtos[['vlr_custo','dat_alteracao','cod_id_produto']].values.tolist())
 
def pipeline_cria_loja():
    print('Criando Loja nova!')
    loja = clock_cria_loja()
    clock_cria_estoque(loja)
    clock_cria_venderores(loja)

# Agendando as funções
schedule.every(30).seconds.do(clock_atualiza_custo_produto).tag('task-mensal')
schedule.every(30).seconds.do(clock_atualiza_saldo_clientes).tag('task-mensal')
schedule.every(30).seconds.do(clock_atualiza_estoque).tag('task-mensal')

schedule.every(20).to(40).seconds.do(pipeline_cria_loja).tag('task-random')
schedule.every(30).to(50).seconds.do(clock_cria_clientes).tag('task-random')
schedule.every(1).to(2).seconds.do(clock_multipla_vendas).tag('task-random')


if __name__ == '__main__':

    limpa_db_sistema()
    cria_produtos()
    pipeline_cria_loja()
    clock_cria_clientes()
    while clock.get_current_time() <= datetime.now():
        print(clock.get_current_time())
        schedule.run_pending()
        time.sleep(1)
