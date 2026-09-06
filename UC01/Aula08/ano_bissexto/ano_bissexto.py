'''
Função que verifica se um ano é ou não bissexto
'''
def eh_bissexto(ano): 
    '''
    Função para conferir se um ano é Bissexto ou não
    '''
    if ano % 4 == 0: 
        if ano % 100 == 0: 
            if ano % 400 == 0: 
                resultado = True 
            else: 
                resultado = False 
        else: 
            resultado = True 
    else: 
        resultado = False 

    return resultado 