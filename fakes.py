from faker import Faker
from faker.providers import BaseProvider
import unicodedata
from classes import Cliente, Estoque, Loja, Vendedor, Produto
from random import  randrange, random, randint

faker = Faker(locale='pt_BR')
faker_pt = Faker(locale='pt_PT')

def choice_probs(elements, probs):

    cumulative_probs = [sum(probs[:i+1]) for i in range(len(probs))]
    rnd = random()

    for i, cp in enumerate(cumulative_probs):
        if rnd < cp:
            return elements[i]

class ClienteProvider(BaseProvider):
    def Cliente(self):
        
        des_nome = faker.first_name()
        des_sobrenome = faker.last_name()
        vlr_poder_compra = randrange(500, 3100, 100)

        nom_email = unicodedata.normalize('NFKD', des_nome.lower().replace(' ','_'))
        sob_nom_email = unicodedata.normalize('NFKD', des_sobrenome.lower().replace(' ','_'))
        nom_email = u"".join([c for c in nom_email if not unicodedata.combining(c)])
        sob_nom_email = u"".join([c for c in sob_nom_email if not unicodedata.combining(c)])

        des_email = '{}_{}@{}'.format(nom_email,sob_nom_email,faker.free_email_domain())
        num_telefone = faker.msisdn()
        dat_nascimento = faker.date_of_birth(minimum_age=15,maximum_age=79)
        
        data_cadastro = None

        return Cliente(
                des_nome= des_nome,
                des_sobrenome= des_sobrenome,
                vlr_poder_compra=vlr_poder_compra,
                vlr_saldo= vlr_poder_compra,
                des_email= des_email,
                num_telefone= num_telefone,
                dat_nascimento= dat_nascimento,
                dat_cadastro= data_cadastro
                )

class EstoqueProvider(BaseProvider):
    def Estoque(self, loja : Loja, produto : Produto):
        qtd_produto = {
           'PEQUENA': randint(10,35),
           'MEDIA': randint(40,75),
           'GRANDE': randint(85,155)
        }
        return Estoque(
            cod_loja = loja.cod_id_loja,
            cod_produto = produto.cod_id_produto,
            qtd_produto = qtd_produto[loja.des_tamanho_loja],
            dat_criacao = loja.dat_criacao,
            dat_alteracao = loja.dat_criacao
            )
               
class LojaProvider(BaseProvider):
    def Loja(self):
        nom_loja = '{} {}'.format(faker_pt.city_name(),faker_pt.company_suffix())
        cod_long, cod_lat, des_bairro, des_pais, des_estado = faker_pt.local_latlng(country_code='BR')
        des_tamanho_loja = choice_probs(['PEQUENA','MEDIA','GRANDE'], [0.7, 0.2, 0.1])
        dat_criacao = faker_pt.date_of_birth(minimum_age=1,maximum_age=5)
        
        return Loja(
                nom_loja = nom_loja,
                cod_long = cod_long,
                cod_lat = cod_lat,
                des_bairro = des_bairro,
                des_pais = des_pais,
                des_estado = des_estado.split('/')[1],
                des_tamanho_loja = des_tamanho_loja,
                dat_criacao = dat_criacao,
                dat_alteracao = dat_criacao
                )
        
class VendedorProvider(BaseProvider):
    def Vendedor(self):
        des_nome = faker.first_name()
        des_sobrenome = faker.last_name()
        nom_email = unicodedata.normalize('NFKD', des_nome.lower().replace(' ','_'))
        sob_nom_email = unicodedata.normalize('NFKD', des_sobrenome.lower().replace(' ','_'))
        nom_email = u"".join([c for c in nom_email if not unicodedata.combining(c)])
        sob_nom_email = u"".join([c for c in sob_nom_email if not unicodedata.combining(c)])
        des_email = '{}_{}@{}'.format(nom_email,sob_nom_email,faker.free_email_domain())
        
        return Vendedor(
                nom_vendedor = f'{des_nome} {des_sobrenome}',
                des_email = des_email,
                cod_loja = None,
                dat_criacao =None,
                dat_alteracao =None)

class ProdutoProvider(BaseProvider):
    def Produto(self):
        nom_produto = ''
        vlr_custo = ''
        des_produto = ''
        des_ticket_price = ''
        dat_criacao = ''
        dat_alteracao = ''
        
        return Produto(
            nom_produto = nom_produto,
            vlr_custo = vlr_custo,
            des_produto = des_produto,
            des_ticket_price = des_ticket_price,
            dat_criacao = dat_criacao,
            dat_alteracao = dat_alteracao
            )

faker.add_provider(ClienteProvider)
faker.add_provider(LojaProvider)
faker.add_provider(VendedorProvider)
faker.add_provider(ProdutoProvider)
faker.add_provider(EstoqueProvider)

# c = faker.Cliente()
# l = faker.Loja()
# v = faker.Vendedor()
# p = faker.Produto()
# e = faker.Estoque(l,p)

# print('done')