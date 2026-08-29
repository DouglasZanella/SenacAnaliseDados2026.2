#Funcao_calc_IMC_ver1.0



def calc_imc (peso, altura):
    '''
    Cálcula o IMC de uma pessoa e retorna um valor float 
    '''
    imc = peso / (altura * altura)
    return imc
