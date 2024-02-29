from infra.repository.cliente_repository import ClienteRepository

repo_cliente = ClienteRepository()
res = repo_cliente.select()

print(res)