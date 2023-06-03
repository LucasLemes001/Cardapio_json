import sqlite3, sqlalchemy, json, flask


with sqlite3.connect('Lista_de_produtos.db') as conexao:
    banco_de_dados = conexao.cursor()
    '''# O comando abaixo irá criar uma tabela dentro do arquivo "Lista_de_produtos.db" com as seguintes colunas:
            * nome_do_produto (que recebera str ou txt)
            * ingrediente_produto (que recebera str ou txt)
            * valor_produto (que recebera float))'''
    # banco_de_dados.execute('create table Produtos(nome_do_produto text, ingrediente_produto text, valor_produto float);')

# FAZER UMA SEQUENCIA ONDE VOU PEGAR
#          NOME DO DOGAO / INGREDIENTES / VALOR
'''
for dicionario in cardapio:
        
        print(dicionario[>>>>'MUDAR AQUI A CHAVE PARA PEGAR INFORMAÇÃO'<<<<<])'''

with open('novocardapio.json','r') as arquivo:   
    cardapio = json.load(arquivo)
    for dicionario in cardapio:   # Para cada 1 dos 31 dicionarios dentro da lista Cardapio....
        nome = dicionario["nome"]   # extrair a chave NOME
        ingrediente = None # Extrair a Lista de ingredientes <<<<<< ESTÁ COM PROBLEMA DE ADD AO BANCO DE DADOS... TRABALHAR EM SOLUCAO>>>>>>>>>>>>
        valor = float(dicionario["preco"]) # extrair a Chave PRECO
        banco_de_dados.execute('insert into Produtos values(?,?,?)',[nome,ingrediente,valor])    # ADICIONANDO AS CHAVES EM SEQUENCIA EM QUE A TABELA TRABALHA (nome_produto/ingrediente_produto/valor_produto)
    conexao.commit()   # SALVANDO AS INFO
        