
import json
from pathlib import Path
from dados import produtos, historico_vendas

# __file__ representa o caminho deste arquivo (persistencia.py).
# Path() transforma esse caminho em um objeto que permite manipulá-lo.
# resolve() obtém o caminho absoluto.
# parent pega a pasta que contém o arquivo, ou seja, 01-Mini-Loja.
PASTA_PROJETO = Path(__file__).resolve().parent

# O operador / junta caminhos quando trabalhamos com objetos Path.
# Assim, loja.json sempre ficará dentro da pasta do projeto,
# independentemente de onde executarmos o programa.
CAMINHO_JSON = PASTA_PROJETO / "loja.json"


def salvar_dados():
    # Reúne as listas compartilhadas em um único dicionário.
    # Esse dicionário será convertido para JSON.
    dados_loja = {
        "produtos": produtos,
        "historico_vendas": historico_vendas
    }

    # Abre o JSON em modo escrita ("w").
    # Se o arquivo não existir, ele será criado.
    # Se já existir, seu conteúdo será sobrescrito.
    # O with fecha o arquivo automaticamente ao sair do bloco.
    with open(CAMINHO_JSON, "w", encoding="utf-8") as arquivo:

        # Converte o dicionário Python para JSON e grava no arquivo.
        # indent=4 deixa o conteúdo organizado.
        # ensure_ascii=False mantém os acentos legíveis.
        json.dump(
            dados_loja,
            arquivo,
            indent=4,
            ensure_ascii=False
        )


def carregar_dados():
    # Tenta recuperar as informações salvas anteriormente.
    try:

        # Abre o arquivo JSON em modo leitura ("r").
        with open(CAMINHO_JSON, "r", encoding="utf-8") as arquivo:

            # Lê o JSON e transforma seu conteúdo em objetos Python.
            # Neste projeto, recuperamos um dicionário com duas listas.
            dados_carregados = json.load(arquivo)

            # Esvazia a lista original de produtos.
            # Não substituímos a lista, pois ela é compartilhada
            # com os outros módulos da Mini Loja.
            produtos.clear()

            # Adiciona à lista os produtos recuperados do JSON.
            produtos.extend(dados_carregados["produtos"])

            # Faz o mesmo processo com o histórico de vendas.
            # Primeiro removemos os registros antigos da memória.
            historico_vendas.clear()

            # Depois inserimos todas as vendas salvas no arquivo.
            historico_vendas.extend(
                dados_carregados["historico_vendas"]
            )

        # Só aparece se a leitura e a atualização terminarem
        # sem lançar uma exceção.
        print("Dados carregados com sucesso!")

    # Se loja.json ainda não existir, não encerramos o programa.
    # A Mini Loja continuará com as listas vazias.
    except FileNotFoundError:
        print(
            "Nenhum arquivo de dados encontrado. "
            "Iniciando loja vazia."
        )
