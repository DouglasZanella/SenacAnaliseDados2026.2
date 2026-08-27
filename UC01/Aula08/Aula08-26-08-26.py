#CÓDIGOS DESENVOLVIDOS EM AULA

# opcao = "s"
# while opcao == "s":


#Definindo Funções:::::
def calculadora_v1(n1,n2,operador="*"):
    # n1 = float(input("Digite o 1° Numero:"))
    # n2 = float(input("Digite o 2° Numero:"))
    # print("Escolha as opção abaixo:")
    # print("\n + para Somar")
    # print("\n - para Somar")
    # print("\n * para Somar")
    # print("\n / para Somar")
    # operador = input("Digite a opção desejada:\n")

    match operador:
        case "+":
            resultado = f"\nA soma entre seus números {n1+n2} é:\n"
           
        case "-":
            resultado = f"\nA subtração entre seus números {n1 - n2} é:\n"
        case "*":
            resultado = f"\nA Multiplicação entre seus números {n1 * n2} é:\n"   
        case "/":
            if n2 != 0:
                resultado = f"\nA Divisão entre seus números {n1 / n2} é:\n"
            else:
                print("Não é possível Divisão por 0")
        case _:
            print("Informe um operdor válido! ")
        
    return resultado
    # print("Deseja continuar?\n"
    #         "\n Digite s para Sim"
    #         "\nDigite n para não"
    #     )
# opcao = input("digite: ")
 
calc = calculadora_v1(333,555)      
print(calc)