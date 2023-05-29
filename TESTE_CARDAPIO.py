'''{
    "Cardapio":{
        "lanches":{
            "tradicionais":[
            ["Simples",["1 Vina", "Maionese", "Ketchup", "Mostarda", "Tomate, Cebola", "Milho", "Batata-Palha"],12.00],
            ["Especial", ["1 Vina", "Maionese", "Ketchup", "Mostarda", "Tomate, Cebola", "Milho","Pepino(Pícles)","Farofa","Queijo-Ralado","Batata-Palha"],12],
            ["Da Casa", ["2 Vinas", "Maionese Temperada" , "Ketchup", "Mostarda", "Tomate, Cebola", "Milho","Pimentão Verde","Batata-Palha"],12]
        ],
            "prensados":[
                ["Catupiry",["1 Vina","Maionese","Tomate","Cebola","Milho","Batata Palha","FRANGO DESFIADO","CATUPIRY"],16.00],
                ["Cheddar",["1 Vina","Maionese","Tomate","Cebola","Milho","Batata Palha","FRANGO DESFIADO","CHEDDAR"],16.00],
                ["4 Queijos",["1 Vina","Maionese","Tomate","Cebola","Milho","Batata Palha","FRANGO DESFIADO","4 QUEIJOS"],16.00],
                ["Pizza",["1 Vina","Maionese","Tomate","Cebola","Milho","Oreano","Batata Palha","PRESUNTO","QUEIJO MUÇARELA"],16.00],
                ["Purê de Batata",["1 Vina","Maionese","Tomate","Cebola","Milho","Pimentão Verde","Batata Palha","PURÊ de Batata"],16.00],
                ["Bacon",["1 Vina","Maionese","Tomate","Cebola","Milho","BACON","Batata Palha"],18.00],
                ["Calabresa",["1 Vina","Maionese","Tomate","Cebola","Milho","CALABRESA","Batata Palha"],18.00],
                ["Cream Cheese",["1 Vina","Maionese","Tomate","Cebola","Milho","Pimentão Verde","FRANGO DESFIADO","CREAM CHEESE","Batata Palha"],19.00]    
            ],
            "premium":[
                ["Provolone Fatiado",["1 Vina","Maionese","Tomate","Cebola","Milho","Pimentão Verde","FRANGO DESFIADO","QUEIJO PROVOLONE","Batata Palha"],18.00],
                ["Carne Queijo",["1 Vina","Maionese","Tomate","Cebola","Milho","CARNE MOÍDA TEMPERADA","QUEIJO MUÇARELA","Batata Palha"],19.00],
                ["Mexicano",["1 Vina","Maionese","Tomate","Cebola","Pimentão Verde","Pimenta Calabresa","CARNE MOÍDA TEMPERADA","CHEDDAR","NACHOS"],19.00]
            ]
        
            },
            "adicionais":[
                ["Vina",2.00],
                ["Farofa",1.00],
                ["Queio Ralado",2.00],
                ["Pepino(Pícles)",2.00],
                ["Cheddar",4.00],
                ["Catupiry",4.00],
                ["4 Queijos",4.00],
                ["Purê",4.00],
                ["Cream Cheese",7.00],
                ["Bacon",6.00],
                ["Calabresa",6.00]
            ],
            "bebidas":[
                ["Refrigerante Lata",5.00],
                ["Suco 500ml",5.00],
                ["Chá copo",5.00],
                ["Água 500ml SEM Gás",3.00],
                ["Água 500ml COM Gás",3.00],
                ["Refrigerante 1 Litro",12.00],
                ["Suco 1 Litro",10.00]
            ]
        }
}

'''


'''ACESSAR SOMENTE O NOME DOS LANCHES....
# for lanche in cardapio["Cardapio"]["lanches"]["prensados"]:

#     print(lanche[0])'''


'''ACESSAR SOMENTE O INGREDIENTES DOS LANCHES ALTERAR O INDICE DENTRO DO PRINT....
#for lanche in cardapio["Cardapio"]["lanches"]["premium"]:
 #   print(lanche[1])'''

import json
from manipular_texto.texto import margem,mensagem_de_erro
from manipular_texto.cor import cores,fonte
'''
with open('dog.json',encoding='utf-8') as json_dog:
    dados = json.load(json_dog)
    print(dados["Cardapio"]["adicionais"])'''



'''Criar DEF para mostrar os lanches de forma espaçada, com os ingredientes e o Valor em R$'''


def printar_cardapio(chaves_do_arquivo,indice_nome_do_lanche,indice_valor_do_lanche,personalizar_Numero_da_iteração):
    for posicao, lanche in enumerate(chaves_do_arquivo):
        print(f'{cores["branco"]}[{posicao+personalizar_Numero_da_iteração}]{cores["amarelo"]+fonte["negrito"]} - {lanche[indice_nome_do_lanche]:^15}{cores["branco"]} R$ {+lanche[indice_valor_do_lanche]:<5.2f}')
    margem(1,'><')
    

def mostrar_cardápio_lanches():
    try:
        with open('dog.json',encoding='utf-8') as arquivo:
            data = json.load(arquivo)
            printar_cardapio(data["Cardapio"]["lanches"]["tradicionais"],0,2,1)
            
            

            printar_cardapio(data["Cardapio"]["lanches"]["prensados"],0,2,4)   
            
            
                
            printar_cardapio(data["Cardapio"]["lanches"]["premium"],0,2,12)
             
            
           
            printar_cardapio(data["Cardapio"]["adicionais"],0,1,1) 
            
            
    except:
        mensagem_de_erro('Não consegui encontrar o Arquivo')



mostrar_cardápio_lanches()
