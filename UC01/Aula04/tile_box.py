#EXERCÍCIO CAIXA DE AZULEIJOS 
'''
Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento,
largura e altura), calcular e escrever a quantidade de caixas de azulejos para se colocar em
todas as suas paredes (considere que não será descontada a área ocupada por portas e
janelas). Cada caixa de azulejos possui 1,5 m²
'''
#codigo tile_box_python_Ver1.0 
altura = float(input("Digite a altura das paredes (em metros): "))

largura = float(input("Digite a largura da parede menor (em metros): ")) 

comprimento = float(input("\nDigite o Comprimento da parede Maior(em metros):"))

#calcular a área:  

Area_total= ((altura*largura)*2) + ((altura*comprimento)*2) 

#calculo da quantidade de caixas 

Qtd_caixas = Area_total / 1.5  

#print("\n A quantidade de caixas de azulejo necessárias para revestir todas as paredes é de  :") 
#print(Qtd_caixas) 

#para imprimir com arredondamento matematico sem importar bibliotecas ou funções é necessário utilizar a lógica matematica e condicional para que ocorra:  

print("\nA quantidade de caixas de azulejo necessárias para revestir todas as paredes é de:") 
print(int(Qtd_caixas) + 1  if Qtd_caixas > int(Qtd_caixas) else int(Qtd_caixas), "caixas") 
