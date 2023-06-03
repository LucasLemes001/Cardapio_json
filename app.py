import sqlite3, sqlalchemy, json, flask


with sqlite3.connect('Lista_de_produtos.db') as conexao:
    banco_de_dados = conexao.cursor()
    # banco_de_dados.execute('create table Produtos(nome_do_produto text, ingrediente_produto text, valor_produto float);')

# FAZER UMA SEQUENCIA ONDE VOU PEGAR
#          NOME DO DOGAO / INGREDIENTES / VALOR
'''
for dicionario in cardapio:
        
        print(dicionario[>>>>'MUDAR AQUI A CHAVE PARA PEGAR INFORMAÇÃO'<<<<<])'''

with open('novocardapio.json','r') as arquivo:
    cardapio = json.load(arquivo)
    for dicionario in cardapio:
        nome = dicionario["nome"]
        ingrediente = None
        valor = float(dicionario["preco"])
        banco_de_dados.execute('insert into Produtos values(?,?,?)',[nome,ingrediente,valor])
    conexao.commit()
        