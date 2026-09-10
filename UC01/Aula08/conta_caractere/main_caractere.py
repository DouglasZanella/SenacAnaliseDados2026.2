#Contar_caractere_python_ver1.0  
from conta_caracatere import contar_caractere

'''
Arquivo principal que chama a função de contagem
'''

print("============================================") 
print("===== Bem-vindo ao contador de caracteres =====") 
print("============================================") 

texto_digitado = input("\nDigite o texto abaixo:\n")  #registra o texto 

caractere_digitado = input("\nAgora digite qual caractere procura:\n") #registra o caractere

quantidade = contar_caractere(texto_digitado, caractere_digitado)#envia os parâmetro para a função e o "contador" da função é retornado e armazenado em "quantidade"
  

print("\n============================================") 
print( 
    f"\nSeu caractere '{caractere_digitado}' " 
    f"aparece {quantidade} vez(es) nesse texto!\n" 
) 