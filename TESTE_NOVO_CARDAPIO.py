import json
with open('novocardapio.json','r') as arquivo:
    cardapio = json.load(arquivo)   # ESSA VARIAVEL RECEBE TODOS OS DADOS DO ARQUIVO JSON FORMATO EM [{}]
    '''
    Dentro de 1 UNICA LISTA temos 31 DICIONARIOS com 3 chaves:
            * nome: STR
            * ingrediente: LIST
            * preco: INT/FLOAT '''
    
    # ACESSANDO NOME DOS PRODUTOS: <<<

    for nome in cardapio:
        print(nome["nome"])

    # ACESSANDO OS INGREDIENTE DOS PRODUTOS: <<<

    for lista_de_ingredientes in cardapio:
        print(lista_de_ingredientes["ingrediente"])
    
    # ACESSANDO O VALOR DOS PRODUTOS: <<<
    for valor in cardapio:
        print(valor["preco"])


    