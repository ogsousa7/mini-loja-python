from dados import historico_vendas

def gerar_relatorio():

    faturamento_total = 0
    unidades_vendidas = 0
    quantidade_por_produto = {}

    for venda in historico_vendas:

        faturamento_total += venda["total"]

        unidades_vendidas += venda["quantidade"]

        if venda["produto"] in quantidade_por_produto:
            quantidade_por_produto[venda["produto"]] += venda["quantidade"]
        else:
            quantidade_por_produto[venda["produto"]] = venda["quantidade"]

    if quantidade_por_produto:
        mais_vendido = max(quantidade_por_produto, key=quantidade_por_produto.get)

        quantidade_mais_vendida = quantidade_por_produto[mais_vendido]

        resultado_mais_vendido = (
            f"{mais_vendido} ({quantidade_mais_vendida} unidades)"
        )
    else:
        resultado_mais_vendido = ("Nenhuma venda realizada ainda!")    

    vendas_realizadas = len(historico_vendas)

    print("\n===== RELATÓRIO DE VENDAS =====")
    print(f"Faturamento total: R$ {faturamento_total:.2f}")
    print(f"Vendas realizadas: {vendas_realizadas}")
    print(f"Unidades vendidas: {unidades_vendidas}")
    print(f"O Produto mais vendido foi: {resultado_mais_vendido}")