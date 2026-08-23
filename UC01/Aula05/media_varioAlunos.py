# #codigo media_variosAlunos_python_Ver1.1 
# #ERROR_FIX 

seunome = input("Digite eu nome: ") 
cont_alunos = int(input("\nQuantos alunos quer registrar? ")) 
print("\n=========================================") 
print(f"\n|{seunome}, os resultados dos alunos são:|") 
print("\n=========================================") 


for i in range(cont_alunos): 
    print(f"\n{i + 1}º ALUNO:") 
    nome_aluno = input("\nDigite o nome do aluno: ") 
    nota1 = float(input("Digite sua primeira nota: ")) 
    nota2 = float(input("Digite sua segunda nota: ")) 
    resp  = input("Você fez a avaliação Optativa? (s/n)?  ") 

    match resp:
        case "s":
            nota_opt = float(input("Digite a nota da sua avaliação optativa: "))
            if nota1 <= nota2 and nota_opt > nota1:
                nota1 = nota_opt
            elif nota2 < nota1 and nota_opt > nota2:
                    nota2 = nota_opt
            media = (nota1+nota2)/2
        case "n":
             media = (nota1+nota2)/2
        case _:
            media = None
            print(f"Resposta inválida, você Digitou {resp}, digite apenas : s ou n")
    if media is None:
        print("\nvolte e digite novamente")
    else:
        if media > 6.0:
            Result_final = "APROVADO!"
        elif media >= 3.0 and media <= 6.0:
            Result_final = "RECUPERAÇÃO!" 
        else:
            Result_final = "REPROVADO!"
        print(f"\nAluno: {nome_aluno}")
        print(f"Média: {media:.2f}")
        print(f"Situação: {Result_final}")
#--------------------------------------------------------------------------------------------------
