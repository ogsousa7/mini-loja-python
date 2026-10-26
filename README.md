# 🛒 Mini Loja — Sistema de Gestão em Python

## 📌 Sobre o projeto

A Mini Loja é um sistema de gerenciamento de produtos e vendas desenvolvido em Python, executado pelo terminal.

O projeto foi criado para consolidar meus conhecimentos de programação, aplicando conceitos como funções, listas, dicionários, módulos, tratamento de exceções e persistência de dados.

## ⚙️ Funcionalidades

- Cadastro de produtos com nome, preço e estoque.
- Listagem dos produtos cadastrados.
- Registro de vendas com verificação de estoque.
- Atualização automática do estoque após cada venda.
- Histórico de vendas com data e hora.
- Relatórios com faturamento total, quantidade de vendas, unidades vendidas e produto mais vendido.
- Salvamento e carregamento de dados utilizando JSON.
- Menu interativo pelo terminal.

## 🛠️ Tecnologias utilizadas

- **Python 3** — linguagem principal.
- **JSON** — armazenamento dos produtos e vendas.
- **datetime** — registro de data e hora.
- **pathlib** — gerenciamento de caminhos.
- **Git e GitHub** — versionamento e publicação do projeto.

## 📂 Estrutura do projeto

```text
01-mini-Loja/
├── main.py
├── dados.py
├── produtos.py
├── vendas.py
├── relatorios.py
├── persistencia.py
├── .gitignore
└── README.md
```

**Responsabilidades dos arquivos:**

- `main.py`: menu principal e interação com o usuário.
- `dados.py`: listas compartilhadas de produtos e vendas.
- `produtos.py`: cadastro e listagem de produtos.
- `vendas.py`: registro de vendas e histórico.
- `relatorios.py`: geração dos indicadores de vendas.
- `persistencia.py`: salvamento e carregamento dos dados em JSON.

O arquivo `loja.json` é criado durante a execução e não é enviado ao repositório.

## ▶️ Como executar

**Pré-requisito:** ter o Python 3 instalado.

1. Clone o repositório ou baixe os arquivos do projeto.
2. Abra um terminal na pasta `01-Mini-Loja`.
3. Execute:

```bash
python main.py
```

No Windows, caso o comando anterior não funcione, tente:

```bash
py main.py
```

O sistema exibirá o menu principal, permitindo cadastrar produtos, registrar vendas e consultar relatórios.

As informações são recuperadas do JSON ao iniciar e salvas quando o usuário escolhe sair pelo menu.

## 📚 Conceitos praticados

Durante o desenvolvimento, pratiquei:

- Lógica de programação.
- Manipulação de listas e dicionários.
- Funções e modularização.
- Estruturas de repetição e condicionais.
- Tratamento de exceções com `try/except`.
- Manipulação de arquivos JSON.
- Referências e mutabilidade de listas.
- Agregação de dados para geração de relatórios.
- Organização e versionamento de projetos.

## 🚀 Possíveis melhorias futuras

- Melhorar a validação de produtos duplicados.
- Implementar salvamento automático após operações importantes.
- Utilizar um banco de dados, como SQLite ou PostgreSQL.
- Desenvolver análises de vendas com Pandas.
- Criar dashboards no Power BI.

## 👨‍💻 Autor

Projeto desenvolvido por Elias Figueiredo de Sousa como parte dos meus estudos de Python e preparação para atuar profissionalmente na área de dados.