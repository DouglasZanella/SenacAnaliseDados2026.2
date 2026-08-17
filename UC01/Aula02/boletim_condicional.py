nome = input("Digite seu nome: ") 

nota1 = float(input("Digite Primeira a nota:")) 
nota2 = float(input("Digite Segunda a nota:")) 
nota3 = float(input("Digite Terceira a nota:")) 
nota4 = float(input("Digite Quarta a nota:")) 

 
media = (nota1+nota2+nota3+nota4) / 4 

if media > 7:
    print(f"{nome}, sua média foi de {media:.2f}, e você está APROVADO\n")
elif media >= 5 and media <= 7:
    print(f"{nome}, sua média foi de {media:.2f} e você está de RECUPERAÇÃO\n Vai estudar!")
else:
    print(f"{nome}, sua média foi de {media:.2f} e você está REPROVADO\n=========================\n")
    print("== YOU SHALL NOT PASS! ==\n")
    print("=========================")