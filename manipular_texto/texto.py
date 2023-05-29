def margem(quantidade_linhas_a_pular,padrao_da_margem):
    for linha_pular in range(quantidade_linhas_a_pular):
        print()
    print(padrao_da_margem*35)

def mensagem_de_erro(Oque_esta_errado):
    print(f'\033[4;31;40mAlgo deu errado! {Oque_esta_errado}!!\033[0m'.center(75, ' '))


    


'''data["Cardapio"]['lanches']['tradicionais'][0][0] endereço p/ Simples, Especial, Da casa... Mudar o penultimo indice
data["Cardapio"]['lanches']['tradicionais'][0][0] endereço p/ Simples, Especial, Da casa... 
'''