from relogio_virtual import RelogioVirtual

class Ambiente:
   def __init__(self,start_year=2024, start_month=1, start_day=1, factor_hour_per_sec=24):
        self.relogio_virtual = RelogioVirtual(start_year, start_month, start_day, factor_hour_per_sec)
   
   def __enter__(self):
        print(f"Entrando no ambiente virtual. Data inicial: {self.relogio_virtual.get_current_time()}")
        return self  # Retorna uma instância de Ambiente para ser usada dentro do bloco 'with'

   def __exit__(self, exc_type, exc_val, exc_tb):
       pass

class Cliente:
    def __init__(self,des_nome, des_sobrenome, vlr_poder_compra, vlr_saldo, des_email, num_telefone, dat_nascimento, dat_cadastro):
        self.des_nome = des_nome
        self.des_sobrenome = des_sobrenome
        self.vlr_poder_compra = vlr_poder_compra
        self.vlr_saldo = vlr_saldo
        self.des_email = des_email
        self.num_telefone = num_telefone
        self.dat_nascimento = dat_nascimento
        self.dat_cadastro = dat_cadastro

    def __repr__(self):
            return f'Cliente (des_nome = {self.des_nome}, des_sobrenome = {self.des_sobrenome}, vlr_poder_compra = {self.vlr_poder_compra}, vlr_saldo = {self.vlr_saldo}, des_email = {self.des_email}, num_telefone = {self.num_telefone}, dat_nascimento = {self.dat_nascimento}, dat_cadastro = {self.dat_cadastro})'
    
    def cria_cliente_fake(clock):
        return 

class Loja:
    def __init__(self,nom_loja, cod_long, cod_lat, des_bairro, des_pais, des_estado, des_tamanho_loja, dat_criacao, dat_alteracao):
        self.nom_loja = nom_loja
        self.cod_long = cod_long
        self.cod_lat = cod_lat
        self.des_bairro = des_bairro
        self.des_pais = des_pais
        self.des_estado = des_estado
        self.des_tamanho_loja = des_tamanho_loja
        self.dat_criacao = dat_criacao
        self.dat_alteracao = dat_alteracao

    def __repr__(self):
            return f'Loja(nom_loja = {self.nom_loja}, cod_long = {self.cod_long}, cod_lat = {self.cod_lat}, des_bairro = {self.des_bairro}, des_pais = {self.des_pais}, des_estado = {self.des_estado}, des_tamanho_loja = {self.des_tamanho_loja}, dat_criacao = {self.dat_criacao}, dat_alteracao = {self.dat_alteracao})'
    
    
    def cria_loja_fake(qtd_lojas,clock):
        ...

class Vendedor:
    def __init__(self,nom_vendedor, des_email, cod_loja, dat_criacao, dat_alteracao):
        self.nom_vendedor =nom_vendedor
        self.des_email =des_email
        self.cod_loja =cod_loja
        self.dat_criacao =dat_criacao
        self.dat_alteracao =dat_alteracao

    def __repr__(self):
            return f'Vendedor(nom_vendedor = {self.nom_vendedor}, des_email = {self.des_email}, dat_criacao = {self.dat_criacao}, dat_alteracao = {self.dat_alteracao})'

    def cria_vendedor_fake(lojas):
        ...

class Estoque:
    def __init__(self,cod_loja, cod_produto, qtd_produto, dat_criacao, dat_alteracao):
        self.cod_loja = cod_loja
        self.cod_produto = cod_produto
        self.qtd_produto = qtd_produto
        self.dat_criacao = dat_criacao
        self.dat_alteracao = dat_alteracao

    def __repr__(self):
            return f'Estoque(cod_loja = {self.cod_loja}, cod_produto = {self.cod_produto}, qtd_produto = {self.qtd_produto}, dat_criacao = {self.dat_criacao}, dat_alteracao = {self.dat_alteracao})'

    def cria_estoque_fake(lojas,produtos):
        ...

class Produto:
    def __init__(self, nom_produto, vlr_custo, des_produto, des_ticket_price, dat_criacao, dat_alteracao):
        self.nom_produto = nom_produto
        self.vlr_custo = vlr_custo
        self.des_produto = des_produto
        self.des_ticket_price = des_ticket_price
        self.dat_criacao = dat_criacao
        self.dat_alteracao = dat_alteracao

    def __repr__(self):
            return f'Produto(nom_produto = {self.nom_produto}, vlr_custo = {self.vlr_custo}, des_produto = {self.des_produto}, des_ticket_price = {self.des_ticket_price}, dat_criacao = {self.dat_criacao}, dat_alteracao = {self.dat_alteracao})'
        
with Ambiente() as ambiente:
    print(ambiente.relogio_virtual.get_current_time())
    pass