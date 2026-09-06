#CONVERSOR DE TEMPERATURA::

from convert_geral import conversor

print("=========================================\n") 
print("Bem-Vindo ao conversor Celcius|Fahrenheit\n") 
print("===========================================") 

controle = "s"
if controle == "s":
    while controle == "s":
            
        print("\n Para converter Celcius em Fahrenheit - Digite 1") 
        print("\n Para converter Fahrenheit em Celcius - Digite 2")
        escolha = int(input("\nQual tipo de conversão deseja realizar?\n")) 

        resultado = conversor(escolha)

        if resultado is not None:
            print(f"\nResultado da conversão: {resultado:.2f}°")

        try:
            print("Deseja converter outra temperatura?")
            controle = input("digite s ou n : \n").lower()
        except ValueError:
            print("Entrada inválida! igite apenas S para Sim e N para não")
else:
    print(
        "Entrada Inválida\n"
        "Obrigado por Usar o CONVERSOR!"
        )
