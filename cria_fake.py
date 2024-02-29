# %%
from faker import Faker
import unicodedata
from random import randint, random, randrange
faker = Faker(locale='pt_BR')

def choice_probs(elements, probs):
    cumulative_probs = [sum(probs[:i+1]) for i in range(len(probs))]
    rnd = random()

    for i, cp in enumerate(cumulative_probs):
        if rnd < cp:
            return elements[i]

def cria_cliente_fake(qtd_clientes, data_cadastro):
    lista_clientes = []
    for _ in range(qtd_clientes):
        des_nome = faker.first_name()
        des_sobrenome = faker.last_name()

        nom_email = unicodedata.normalize('NFKD', des_nome.lower().replace(' ','_'))
        sob_nom_email = unicodedata.normalize('NFKD', des_sobrenome.lower().replace(' ','_'))
        nom_email = u"".join([c for c in nom_email if not unicodedata.combining(c)])
        sob_nom_email = u"".join([c for c in sob_nom_email if not unicodedata.combining(c)])

        des_email = '{}_{}@{}'.format(nom_email,sob_nom_email,faker.free_email_domain())
        num_telefone = faker.msisdn()
        dat_nascimento = faker.date_of_birth(minimum_age=15,maximum_age=79)
        vlr_poder_compra = randrange(500, 3100, 100)
        lista_clientes.append({'des_nome': des_nome,
                'des_sobrenome': des_sobrenome,
                'vlr_poder_compra':vlr_poder_compra,
                'vlr_saldo': vlr_poder_compra,
                'des_email': des_email,
                'num_telefone': num_telefone,
                'dat_nascimento': dat_nascimento,
                'dat_cadastro': data_cadastro
                })
        
    return lista_clientes

def cria_loja_fake(qtd_lojas,clock):
    lista_lojas = []
    for _ in range(qtd_lojas):
        faker_pt = Faker(locale='pt_PT')
        nom_loja = '{} {}'.format(faker_pt.city_name(),faker_pt.company_suffix())
        cod_long, cod_lat, des_bairro, des_pais, des_estado = faker.local_latlng(country_code='BR') #cod_long, cod_lat, des_bairro, des_pais, des_estado
        des_tamanho_loja = choice_probs(['PEQUENA','MEDIA','GRANDE'], [0.7, 0.2, 0.1])
        dat_criacao = faker.date_of_birth(minimum_age=1,maximum_age=5)
        
        lista_lojas.append({'nom_loja':nom_loja,
                'cod_long':cod_long,
                'cod_lat':cod_lat,
                'des_bairro':des_bairro,
                'des_pais':des_pais,
                'des_estado':des_estado,
                'des_tamanho_loja':des_tamanho_loja,
                'dat_criacao':clock.get_current_time() or dat_criacao,
                'dat_alteracao':clock.get_current_time() or dat_criacao})
        
    return lista_lojas

def cria_vendedor_fake(lojas):
    lista_vendedores = []
    for _, loja_row in lojas.iterrows():
        if loja_row['des_tamanho_loja'] == 'PEQUENA':
            for _ in range(randint(1,2)): #QUANTIDADE DE VENDEDORES
                des_nome = faker.first_name()
                des_sobrenome = faker.last_name()
                nom_email = unicodedata.normalize('NFKD', des_nome.lower().replace(' ','_'))
                sob_nom_email = unicodedata.normalize('NFKD', des_sobrenome.lower().replace(' ','_'))
                nom_email = u"".join([c for c in nom_email if not unicodedata.combining(c)])
                sob_nom_email = u"".join([c for c in sob_nom_email if not unicodedata.combining(c)])
                des_email = '{}_{}@{}'.format(nom_email,sob_nom_email,faker.free_email_domain())
                lista_vendedores.append({'nom_vendedor': f'{des_nome} {des_sobrenome}',
                                        'des_email': des_email,
                                        'cod_loja': loja_row['cod_id_loja'],
                                        'dat_criacao':loja_row['dat_criacao'],
                                        'dat_alteracao':loja_row['dat_criacao']})
        if loja_row['des_tamanho_loja'] == 'MEDIA':
            for _ in range(randint(3,7)): #QUANTIDADE DE VENDEDORES
                des_nome = faker.first_name()
                des_sobrenome = faker.last_name()
                nom_email = unicodedata.normalize('NFKD', des_nome.lower().replace(' ','_'))
                sob_nom_email = unicodedata.normalize('NFKD', des_sobrenome.lower().replace(' ','_'))
                nom_email = u"".join([c for c in nom_email if not unicodedata.combining(c)])
                sob_nom_email = u"".join([c for c in sob_nom_email if not unicodedata.combining(c)])
                des_email = '{}_{}@{}'.format(nom_email,sob_nom_email,faker.free_email_domain())
                lista_vendedores.append({'nom_vendedor': f'{des_nome} {des_sobrenome}',
                                        'des_email': des_email,
                                        'cod_loja': loja_row['cod_id_loja'],
                                        'dat_criacao':loja_row['dat_criacao'],
                                        'dat_alteracao':loja_row['dat_criacao']})
        if loja_row['des_tamanho_loja'] == 'GRANDE':
            for _ in range(randint(12,20)): #QUANTIDADE DE VENDEDORES
                des_nome = faker.first_name()
                des_sobrenome = faker.last_name()
                nom_email = unicodedata.normalize('NFKD', des_nome.lower().replace(' ','_'))
                sob_nom_email = unicodedata.normalize('NFKD', des_sobrenome.lower().replace(' ','_'))
                nom_email = u"".join([c for c in nom_email if not unicodedata.combining(c)])
                sob_nom_email = u"".join([c for c in sob_nom_email if not unicodedata.combining(c)])
                des_email = '{}_{}@{}'.format(nom_email,sob_nom_email,faker.free_email_domain())
                lista_vendedores.append({'nom_vendedor': f'{des_nome} {des_sobrenome}',
                                        'des_email': des_email,
                                        'cod_loja': loja_row['cod_id_loja'],
                                        'dat_criacao':loja_row['dat_criacao'],
                                        'dat_alteracao':loja_row['dat_criacao']})
                
    return lista_vendedores

def cria_estoque_fake(lojas,produtos):

    lista_estoques = []
    for _, loja_row in lojas.iterrows():
        
        if loja_row['des_tamanho_loja'] == 'PEQUENA':
            l_produtos = produtos.sample(n=randint(1,round(len(produtos)*0.1)))
            for _, prod_row in l_produtos.iterrows():
                lista_estoques.append({'cod_loja':loja_row['cod_id_loja'],
                                    'cod_produto':prod_row['cod_id_produto'],
                                    'qtd_produto':randint(10,35),
                                    'dat_criacao':loja_row['dat_criacao'],
                                    'dat_alteracao':loja_row['dat_criacao']})
                
        if loja_row['des_tamanho_loja'] == 'MEDIA':
            l_produtos = produtos.sample(n=randint(1,round(len(produtos)*0.3)))
            for _, prod_row in l_produtos.iterrows():
                lista_estoques.append({'cod_loja':loja_row['cod_id_loja'],
                                    'cod_produto':prod_row['cod_id_produto'],
                                    'qtd_produto':randint(40,75),
                                    'dat_criacao':loja_row['dat_criacao'],
                                    'dat_alteracao':loja_row['dat_criacao']})
                
        if loja_row['des_tamanho_loja'] == 'GRANDE':
            l_produtos = produtos.sample(n=randint(1,round(len(produtos)*0.7)))
            for _, prod_row in l_produtos.iterrows():
                lista_estoques.append({'cod_loja':loja_row['cod_id_loja'],
                                    'cod_produto':prod_row['cod_id_produto'],
                                    'qtd_produto':randint(85,155),
                                    'dat_criacao':loja_row['dat_criacao'],
                                    'dat_alteracao':loja_row['dat_criacao']})
    return lista_estoques

#print(cria_loja_fake())
#print(cria_cliente_fake())
#print(cria_vendedor_fake())
# loja = cria_loja_fake()
# estoque = cria_estoque_fake(loja)

# print(loja['des_tamanho_loja'])
# print(len(estoque))
# %%

# for i in [4,5,8,10,12,14]:
#     for _ in range(randint(2,7)):
#         # c = cria_cliente_fake()
#         q = '({},{},{},{}),'.format(i,choice([1,2,3]),randint(3,8), round(random()*100,2) )
#         print(q)
# PARA PRODUTO VOU CRIAR NOMES REAIS E O VALOR VOU FAZER UM SCRAPING DA BOLSA DE VALORES
# def cria_produto():
# nom_produto
# vlr_preco
# des_produto

# %%
# VOU BUSCAR NA BASE DE DADOS E FAZER 'COMPRAS ALEATÓRIAS'
# def cria_venda():
# cod_loja
# cod_vendedor
# cod_produto
# qtd_produto
# cod_id_cliente



# def inicia_ambiente():
#AQUI EU VOU INICIAR AS LOJAS -> PRODUTOS (46 ITENS PRA LOJAS GRANDES (80% DOS PRODS))
# %%

# %%
