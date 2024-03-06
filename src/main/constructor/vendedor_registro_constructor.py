from src.views.vendedor_registro_view import VendedorCadastroView
from src.controllers.vendedor_registro_controller import VendedorCadastroController

def vendedor_registro_constructor():
    lojas = VendedorCadastroController.busca_lojas()  
    vendedor_registro_view = VendedorCadastroView(lojas)
    vendedor_registro_controller = VendedorCadastroController()

    info_vendedor = vendedor_registro_view.cadastro_vendedor_view()
    response = vendedor_registro_controller.cadastra(info_vendedor)

    if response["success"]:
        vendedor_registro_view.cadastro_vendedor_sucesso(response["message"])
    else:
        vendedor_registro_view.cadastro_vendedor_falha(response["error"])
