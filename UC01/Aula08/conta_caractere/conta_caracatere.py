 #Contar_caractere_python_ver1.0  

def contar_caractere(texto, caractere_procurado): 
    '''
    Função que recebe o texto digitado e o caratere procurado e compara os dois para verificar a quantidade de vezes
    que o caractere aparee na String, ele recebe os parâmetros lá do arquivo principal e aqui ele só 
    procura e compara e soma 1 no contador para poder verificar quantos caracteres iguais tem
    '''
    contador = 0 
    for caractere_atual in texto: #For i in J (para cada elemento da String)
        if caractere_atual.lower() == caractere_procurado.lower(): 
            contador = contador + 1 
    return contador #retorna o contador com todos os "+1" somados