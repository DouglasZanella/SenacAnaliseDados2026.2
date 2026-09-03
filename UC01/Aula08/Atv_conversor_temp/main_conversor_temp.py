#CONVERSOR DE TEMPERATURA::

from convert_geral import conversor

print("=========================================\n") 
print("Bem-Vindo ao conversor Celcius|Fahrenheit\n") 
print("===========================================") 

print("\n Para converter Celcius em Fahrenheit - Digite 1") 
print("\n Para converter Fahrenheit em Celcius - Digite 2")
escolha = int(input("\nQual tipo de conversão deseja realizar?\n")) 

conversor(escolha)