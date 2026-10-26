from produtos import cadastrar_produto, listar_produtos
from vendas import registrar_venda, listar_vendas
from relatorios import gerar_relatorio
from persistencia import salvar_dados, carregar_dados

carregar_dados()

while True:
    print("\n===== MINI LOJA =====")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Registrar venda")
    print("4 - Listar vendas")
    print("5 - Gerar relatorio")
    print("6 - Sair \n")

    try:
        escolha = int(input("Escolha: "))
    except ValueError:
        print("\nDigite valores numericos validos!")
        continue

    if escolha == 1:

        nome = input("Nome: ").strip()

        try:
            preco = float(input("Preco: "))
            estoque = int(input("Estoque: "))
        except ValueError:
            print("\nDigite valores numericos validos!")
            continue # não usei break para não quebrar o While inteiro

        if preco <= 0 or estoque < 0:
            print("\nPRODUTO NÃO CADASTRADO, preco ou estoque menor que zero!")
        else:
            cadastrar_produto(nome, preco, estoque)
            print("\nProduto cadastrado!")

    elif escolha == 2:

        listar_produtos()

    elif escolha == 3:
    
        nome_produto = input("Qual produto deseja comprar? ")    
        registrar_venda(nome_produto)

    elif escolha == 4:

        listar_vendas()

    elif escolha == 5:

        gerar_relatorio()    

    elif escolha == 6:

        print("\nSaindo...")

        salvar_dados()
        break

    else: 
        print("\nEscolha um numero valido!")