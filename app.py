import sqlite3, sqlalchemy, json, flask


# with sqlite3.connect('Lista_de_produtos.db') as conexao:
    # banco_de_dados = conexao.cursor()
    # banco_de_dados.execute('create table Produtos(nome_do_produto text, ingrediente_produto text, valor_produto float);')

# FAZER UMA SEQUENCIA ONDE VOU PEGAR
#          NOME DO DOGAO / INGREDIENTES / VALOR

with open('dog.json','r') as arquivo:
    cardapio = json.load(arquivo)
    
    for lanche in cardapio["Cardapio"]["lanches"]["tradicionais"]:
        nome = lanche
        print(nome)