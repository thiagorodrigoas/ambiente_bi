from src.views.produto_registro_view import ProdutoCadastroView
from src.controllers.produto_registro_controller import ProdutoRegistroController

def produto_cadastro_constructor():
    produto_cadastro_view = ProdutoCadastroView()
    produto_registro_controller = ProdutoRegistroController()

    info_produto_nova = produto_cadastro_view.cadastro_produto_view()
    response = produto_registro_controller.register(info_produto_nova)

    if response["success"]:
        produto_cadastro_view.cadastro_produto_sucesso(response["message"])
    else:
        produto_cadastro_view.cadastro_produto_falha(response["error"])