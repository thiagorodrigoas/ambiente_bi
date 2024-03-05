from src.views.loja_encontra_view import LojaEncontraView
from src.controllers.loja_encontra_controller import LojaEncontraController

def loja_encontra_constructor():
    loja_encontra_view = LojaEncontraView()
    loja_encontra_controller = LojaEncontraController()

    info_loja_busca = loja_encontra_view.encontra_loja_view()
    response = loja_encontra_controller.encontra(info_loja_busca)

    if response["success"]:
        loja_encontra_view.encontra_loja_sucesso(response["message"])
    else:
        loja_encontra_view.encontra_loja_falha(response["error"])
