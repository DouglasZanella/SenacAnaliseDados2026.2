#codigo media_variosAlunos_python_Ver1.4 
#UPDATE 

seunome = input("Digite eu nome: ") 
cont_alunos = int(input("\nQuantos alunos quer registrar? ")) 
print("\n=========================================") 
print(f"\n|{seunome}, os resultados dos alunos são:|") 
print("\n=========================================") 
Lista_alunos = [] 

for i in range(cont_alunos): 
    print(f"\n{i + 1}º ALUNO:") 
    Nome_aluno = input("\nDigite o nome do aluno: ") 
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
            Lista_alunos.append(f"Aluno{i+1}: {Nome_aluno} - {Result_final}") 
        elif media >= 3.0 and media <= 6.0: 
            Result_final = "RECUPERAÇÃO!" 
            Lista_alunos.append(f"Aluno{i+1}: {Nome_aluno} - {Result_final}") 
        else: 
            Result_final = "REPROVADO!" 
            Lista_alunos.append(f"Aluno{i+1}: {Nome_aluno} - {Result_final}") 

print("\nA listagem dos aunos é:") 
for aluno in Lista_alunos: 
    print(aluno)
#MOSTRA APENAS OS ALUNOS APROVADOS

# for aluno in Lista_alunos: 
#     if "APROVADO" in aluno: #só vai imprimir os ALUNOS APROVADOS
#         print(aluno)
