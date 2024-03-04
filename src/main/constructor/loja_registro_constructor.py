from src.views.loja_registro_view import LojaCadastroView
from src.controllers.loja_registro_controller import LojaRegistroController

def loja_cadastro_constructor():
    loja_cadastro_view = LojaCadastroView()
    loja_registro_controller = LojaRegistroController()

    info_loja_nova = loja_cadastro_view.cadastro_loja_view()
    response = loja_registro_controller.register(info_loja_nova)

    if response["success"]:
        loja_cadastro_view.cadastro_loja_sucesso(response["message"])
    else:
        loja_cadastro_view.cadastro_loja_falha(response["error"])