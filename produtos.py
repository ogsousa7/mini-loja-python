from dados import produtos

def cadastrar_produto(nome, preco, estoque):
    dicionario_produtos = {
        "nome": nome,
        "preco": preco,
        "estoque": estoque
    }

    produtos.append(dicionario_produtos)


def listar_produtos():
    if len(produtos) == 0:
        return print("\nNenhum produto cadastrado!")

    print("\n===== PRODUTOS CADASTRADOS =====")
    for indice, produto in enumerate(produtos, start=1):
        print(f"{indice}. {produto["nome"]} | R$ {produto["preco"]:.2f} | Estoque: {produto["estoque"]}")