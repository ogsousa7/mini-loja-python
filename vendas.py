from datetime import datetime
from dados import produtos, historico_vendas
from produtos import listar_produtos

def registrar_venda(nome_produto):
    listar_produtos()

    for produto in produtos:
        if produto["nome"].lower() == nome_produto.lower():
            print(f"Produto '{produto["nome"]}' encontrado!")

            try:
                quantidade_desejada = int(input("Quantos produtos deseja? "))
            except ValueError:
                print("Digite um valor numerico!")
                return

            if quantidade_desejada <= 0:
                print("Venda recusada!")
                return 

            if quantidade_desejada > produto["estoque"]:
                print("Não há estoque suficiente!")
                return

            produto["estoque"] -= quantidade_desejada

            total_venda = quantidade_desejada * produto["preco"]

            print(f"Valor total da venda: R${total_venda:.2f}")    

            agora = datetime.now()

            salvar_venda(produto["nome"], quantidade_desejada, produto["preco"], total_venda, agora.strftime("%d/%m/%Y %H:%M:%S"))

            return
        
    print("Produto inexistente!")




def salvar_venda(produto, quantidade, preco_unitario, total, data):

    dicionario_historico = {
        "produto": produto,
        "quantidade": quantidade,
        "preco_unitario": preco_unitario,
        "total": total,
        "data": data
    }

    historico_vendas.append(dicionario_historico)


def listar_vendas():

    if len(historico_vendas) == 0:
            return print("\nNenhum historico cadastrado!")
    
    print("\n===== HISTORICO VENDAS =====")
    for indice, historico_venda in enumerate(historico_vendas, start=1):
        print(
            f"{indice}. {historico_venda['produto']} | "
            f"Quantidade: {historico_venda['quantidade']} | "
            f"Preço unitário: R$ {historico_venda['preco_unitario']:.2f} | "
            f"Total: R$ {historico_venda['total']:.2f} | "
            f"Data: {historico_venda['data']}"
        )