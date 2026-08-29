#Funcao_classificacao_IMC_ver1.0

def classificacao(imc):
    '''
    Compara os valores da funcao IMC para classificar a faixa de uma deternminada pessoa.
    '''
    if imc < 18.5:
        classificacao = f"Abaixo do Peso"
    elif imc >= 18.5 and imc <= 24.9:
        classificacao = f"Com Peso Normal"
    elif imc >= 25 and imc <= 29.9:
        classificacao = f"Com Sobrepeso"
    else:
        classificacao = f"Com Obesidade"
    return classificacao
