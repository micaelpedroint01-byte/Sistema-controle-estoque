produtos = []

def cadastrar_produto(nome, quantidade):
    produto = {
        "nome": nome,
        "quantidade": quantidade
    }

    produtos.append(produto)
    print(f"Produto {nome} cadastrado com sucesso!")

def listar_produtos():
    print("\n=== PRODUTOS CADASTRADOS ===")

    for produto in produtos:
        print(
            f"Produto: {produto['nome']} | "
            f"Quantidade: {produto['quantidade']}"
        )