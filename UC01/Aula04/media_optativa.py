'''
#codigo media_com_optativa_Ver1.0 
nome = input("Digite eu nome: ") 
nota1 = float(input("Digite sua primeira nota: ")) 
nota2 = float(input("Digite sua primeira nota: ")) 
resp  = input("Você fez a avaliação Optativa? (s/n)?  ") 

match resp:
    case "s":
        Nota_opt = float(input("Digite a nota da sua avaliação optativa: "))
        if nota1<=nota2:
            if nota_opt>nota1:
                nota1 = nota_opt 
            else:
                if nota_opt>nota2:
                    nota2 = nota_opt 
        media = (nota1+nota2)/2
    case "n":
        media = (nota1+nota2)/2
    case _:
        media = 0
        print(f"Resposta inválida, você Digitou {resp}, digite apenas : s ou n") 

if media == 0:
    print("\nvolte e digite novamente")
else:
    if media > 6.0:
        print(f"\n {nome} , sua média foi de {media}, portanto você está APROVADO!") 
    elif media >= 3.0 and media <= 6.0:
        print(f"\n {nome} , sua média foi de {media}, portanto você está de RECUPERAÇÃO!")
    else:
        print(f"\n {nome} , sua média foi de {media}, portanto você está de REPROVADO!") 
 #---------------- AQUI ENCERRA O QUE FOI PEDIDO -------------------------
 '''
#codigo media_com_optativa_Ver1.1 
nome = input("Digite eu nome: ") 
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
        print(f"\n {nome} ,suas notas são: {nota1,nota2}") 
        print(f"\ne sua média foi de {media}, portanto você está de APROVADO!") 
    elif media >= 3.0 and media <= 6.0: 
        print(f"\n {nome} ,suas notas são: {nota1,nota2}") 
        print(f"\ne sua média foi de {media}, portanto você está de RECUPERAÇÃO!") 
    else: 
        print(f"\n {nome} ,suas notas são: {nota1,nota2}") 
        print(f"\ne sua média foi de {media}, portanto você está de REPROVADO!\n")
