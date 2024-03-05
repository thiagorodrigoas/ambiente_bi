from src.views.vendedor_encontra_view import VendedorEncontraView
from src.controllers.vendedor_encontra_controller import VendedorEncontraController

def vendedor_encontra_constructor():
    vendedor_encontra_view = VendedorEncontraView()
    vendedor_encontra_controller = VendedorEncontraController()

    info_vendedor_busca = vendedor_encontra_view.encontra_vendedor_view()
    response = vendedor_encontra_controller.encontra(info_vendedor_busca)

    if response["success"]:
        vendedor_encontra_view.encontra_vendedor_sucesso(response["message"])
    else:
        vendedor_encontra_view.encontra_vendedor_falha(response["error"])
