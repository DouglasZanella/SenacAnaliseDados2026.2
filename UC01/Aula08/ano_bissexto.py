#Ano_Bissexto_python_ver1.0  

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

controle = "s"
while controle == "s":
    ano_digitado = int(input("Digite o ano que deseja verificar:\n")) 
    resultado = eh_bissexto(ano_digitado) 
        
    controle = (input("Deseja Continuar? (s/n): \n")).lower()
   
    

if resultado: 
    print(f"\nO ano {ano_digitado} é bissexto!") 
else: 
    print(f"\nO ano {ano_digitado} não é bissexto!")
