#CÓDIGOS DESENVOLVIDOS DURANTE A AULA 
#mes = input("Informe o mês de seu nascimento: (1 a 12):")
mes = int(input("Informe o mês de seu nascimento: (1 a 12):")) #para uso do MATCH 

# if mes==str(1):#lembrar de converter a entrada do usuário para string para que possa rodar melhor.
#     signo="Aquário"
# elif mes==str(2):
#     signo="Peixes"
# elif mes==str(3):
#     signo="Áries"
# elif mes==str(4):
#     signo="Touro"
# elif mes==str(5):
#     signo="Gêmeos"
# elif mes==str(6):
#     signo="Câncer"
# elif mes==str(7):
#     signo="Leão"
# elif mes==str(8):
#     signo="Virgem"
# elif mes==str(9):
#     signo="Libra"
# elif mes==str(10):
#     signo="Escorpião"
# elif mes==str(11):
#     signo="Sagitário"
# elif mes==str(12):
#     signo="Capricórnio"
# else:
#     print("Digite um número válido de 1 a 12")

# print(f"Seu signo é {signo}.")

match mes:
    case 1:
        signo = "Aquário"
    case 2:
        signo="Peixes"
    case 3:
        signo="Áries"
    case 4:
        signo="Touro"
    case 5:
        signo="Gêmeos"
    case 6:
        signo="Câncer"
    case 7:
        signo="Leão"
    case 8:
        signo="Virgem"
    case 9:
        signo="Libra"
    case 10:
        signo="Escorpião"
    case 11:
        signo="Sagitário"
    case 12:
        signo="Capricórnio"
    case _:
        signo="Número de mês inválido"
        
print(f"{signo}.")