#Ano_Bissexto_python_ver1.1
#UPGRADE 

from ano_bissexto import eh_bissexto

controle = "s"
while controle == "s":
    ano_digitado = int(input("Digite o ano que deseja verificar:\n")) 
    resultado = eh_bissexto(ano_digitado) 
    if resultado: 
        print(f"\nO ano {ano_digitado} é bissexto!") 
    else: 
        print(f"\nO ano {ano_digitado} não é bissexto!")
        
    controle = (input("Deseja Continuar? (s/n): \n")).lower()
    if controle == "n":
        print(
            "SAINDO DO PROGRAMA..."
            "\nObrigado por usar o programa!"
        )