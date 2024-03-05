from faker import Faker
from faker.providers import BaseProvider
import unicodedata
from datetime import datetime
from src.models.entities import Cliente, Estoque, Loja, Vendedor, Produto
from random import  randrange, random, randint, choice
import pandas as pd
import yfinance as yf

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
    stock_tickers = ["ABEV3.SA",
                        "AZUL4.SA",
                        "B3SA3.SA",
                        "BBAS3.SA",
                        "BBDC3.SA",
                        "BBDC4.SA",
                        "BBSE3.SA",
                        "BRAP4.SA",
                        "BRFS3.SA",
                        "BRKM5.SA",
                        "CCRO3.SA",
                        "CIEL3.SA",
                        "CMIG4.SA",
                        "COGN3.SA",
                        "CSAN3.SA",
                        "CSNA3.SA",
                        "CVCB3.SA",
                        "CYRE3.SA",
                        "ECOR3.SA",
                        "EGIE3.SA",
                        "ELET3.SA",
                        "ELET6.SA",
                        "EMBR3.SA",
                        "ENBR3.SA",
                        "EQTL3.SA",
                        "FLRY3.SA",
                        "GGBR4.SA",
                        "GOAU4.SA",
                        "GOLL4.SA",
                        "HYPE3.SA",
                        "IRBR3.SA",
                        "ITSA4.SA",
                        "ITUB4.SA",
                        "JBSS3.SA",
                        "KLBN11.SA",
                        "LREN3.SA",
                        "MGLU3.SA",
                        "MRFG3.SA",
                        "MRVE3.SA",
                        "MULT3.SA",
                        "NTCO3.SA",
                        "PCAR3.SA",
                        "PETR3.SA",
                        "PETR4.SA",
                        "QUAL3.SA",
                        "RADL3.SA",
                        "RENT3.SA",
                        "SANB11.SA",
                        "SBSP3.SA",
                        "SUZB3.SA",
                        "TAEE11.SA",
                        "TOTS3.SA",
                        "UGPA3.SA",
                        "USIM5.SA",
                        "VALE3.SA",
                        "VIVT3.SA",
                        "WEGE3.SA",
                        "YDUQ3.SA"]
    list_products =[("Espada de Fogo", "Uma espada encantada que inflama ao comando."),
            ("Armadura Etérea", "Armadura leve que oferece proteção contra ataques espirituais."),
            ("Pergaminho do Dragão", "Contém um feitiço poderoso, ainda indecifrado."),
            ("Poção de Cura", "Restaura pequenas quantidades de pontos de vida."),
            ("Anel de Invisibilidade", "Torne-se invisível por curtos períodos."),
            ("Elmo do Falcão", "Melhora a visão e percepção do usuário."),
            ("Botas Aladas", "Permite ao usuário levitar por curtos períodos."),
            ("Amuleto da Sorte", "Aumenta a chance de acertos críticos."),
            ("Manto das Sombras", "Concede habilidades de furtividade."),
            ("Lança Relâmpago", "Pode eletrocutar inimigos ao contato."),
            ("Escudo de Gaia", "Um escudo que absorve ataques mágicos."),
            ("Dardo Encantado", "Nunca erra o alvo."),
            ("Baú do Ladrão", "Pequeno baú que pode conter itens valiosos."),
            ("Cetro Lunar", "Amplifica habilidades mágicas relacionadas à lua."),
            ("Tomo dos Mortos", "Permite ao usuário comunicar-se com espíritos."),
            ("Bálsamo Restaurador", "Cura doenças e venenos."),
            ("Arco Solar", "Seus tiros são feitos de pura luz."),
            ("Diadema de Sereia", "Permite respirar debaixo d'água."),
            ("Manoplas do Ogro", "Aumenta a força física do usuário."),
            ("Bastão de Oráculo", "Revela o futuro próximo."),
            ("Pedra Telepática", "Permite comunicação mental."),
            ("Máscara da Noite", "Concede visão noturna."),
            ("Flauta Hipnótica", "Pode colocar inimigos em transe."),
            ("Capa de Voo", "Permite ao usuário voar."),
            ("Frasco de Névoa", "Libera uma névoa densa para fuga rápida."),
            ("Grimório Elemental", "Livro de feitiços de elementais."),
            ("Adaga do Assassino", "Extremamente afiada e quase indetectável."),
            ("Bola de Cristal", "Usada para espiar lugares distantes."),
            ("Cordão do Tempo", "Pode retardar ou acelerar o tempo ao redor do usuário."),
            ("Bracelete de Gelo", "Concede resistência ao frio e pode congelar inimigos."),
            ("Tocha Eterna", "Uma tocha que nunca se apaga."),
            ("Moeda da Fortuna", "Decide o resultado de uma escolha ao ser lançada."),
            ("Pena de Grifo", "Usada para escrever contratos mágicos."),
            ("Relicário da Vida", "Pode reviver uma pessoa uma única vez."),
            ("Broche de Fala", "Permite falar e compreender qualquer língua."),
            ("Bainha Mágica", "Qualquer espada colocada se torna afiada e encantada."),
            ("Pederneira de Fênix", "Cria fogo que nunca se extingue."),
            ("Tiara da Sabedoria", "Aumenta a inteligência e conhecimento do usuário."),
            ("Óleo de Hermes", "Acelera objetos quando aplicado."),
            ("Talismã do Retorno", "Teleporta o usuário para um local pré-determinado."),
            ("Selo do Silêncio", "Previne magias de serem lançadas nas proximidades."),
            ("Colar da Resistência", "Protege contra maldições e encantamentos."),
            ("Harpa Celestial", "Sons podem curar feridas e acalmar corações."),
            ("Frasco de Vento", "Libera fortes rajadas de vento."),
            ("Pergaminho Vazio", "Pode armazenar qualquer feitiço escrito nele."),
            ("Sino do Acordar", "Desperta qualquer um de um sono profundo."),
            ("Corda Infinita", "Estende-se tanto quanto o usuário precisar."),
            ("Cajado de Energia", "Amplifica feitiços de ataque do usuário."),
            ("Anel de Teleporte", "Teleporta o usuário para locais conhecidos."),
            ("Flecha Fantasma", "Passa através de objetos sólidos."),
            ("Varinha da Ilusão", "Cria ilusões realísticas."),
            ("Martelo de Eco", "Produz um som ensurdecedor ao atingir."),
            ("Cinto de Levitação", "Eleva o usuário acima do solo."),
            ("Botas do Deserto", "Previne exaustão em climas quentes."),
            ("Garrafa de Tempestade", "Pode convocar uma tempestade quando aberta."),
            ("Espelho de Verdade", "Revela a verdadeira forma de qualquer um refletido nele."),
            ("Lira de Encantamento", "Encanta quem ouve sua melodia."),
            ("Máscara do Medo", "Induz terror em quem a observa.")]

    def get_vlr_custo(self, tck, data_consulta):
        # Define o período de data_consulta até hoje
        end_date = pd.Timestamp.today()
        print(f'Baixando dados da ação: {tck}')
        daily_data = yf.download(tck, start=data_consulta, end=end_date)
        

        daily_data = daily_data['Close']
        #daily_data = daily_data.apply(lambda row: row.fillna(row.mean()), axis=1)
        daily_data = daily_data.round(2)
        daily_data =  daily_data.reset_index() 
        daily_data['Date'] = daily_data['Date'].dt.strftime('%Y-%m-%d')
        dat_referencia, price = list(daily_data.values[0])
        return dat_referencia, price

    def Produto(self):
        item_produto = choice(self.list_products)
        ticker = choice(self.stock_tickers)
        dt_hoje = datetime.now()
        dat_referencia, price = self.get_vlr_custo(ticker, dt_hoje)


        nom_produto = item_produto[0]
        vlr_custo = price
        des_produto = item_produto[1]
        des_ticket_price = ticker
        dat_criacao = dat_referencia
        dat_alteracao = dat_referencia
        
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