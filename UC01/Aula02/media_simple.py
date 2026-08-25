#Media_Simples_Python(ver1.0): 
nome = input("Digite o  nome do aluno: ")
nota1 = float(input("Digite Primeira a nota:"))
nota2 =  float(input("Digite Segunda nota:"))
nota3 =  float(input("Digite Terceira nota:"))
nota4 =  float(input("Digite Quarta nota:"))
media = (nota1+nota2+nota3+nota4) / 4 
print("A média do aluno", nome, " é: ",media) 

if media > 7: 
    print("o aluno está APROVADO!\n")
elif media >=5 and media < 7: 
    print("o aluno está de RECUPERAÇÃO!\n") 
else: 
    print("o Aluno está REPROVADO!\n") 

 