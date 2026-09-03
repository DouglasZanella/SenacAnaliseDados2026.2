#DESAFIO DE CONVERTER QUALQUER UMA DAS TEMPERATURAS
# from convert_c_f import celcius_fahrenheit
# from convert_f_c import fahrenheit_celcius

# def conversores(escolha):
#     if escolha == 1: 
#         temp_digitada = float(input("Digite o valor a ser convertido:\n")) 
#         resultado = f"\nResultado: conversores(temp_digitada) {celcius_fahrenheit:.2f} °F\n"
#         return resultado 
#     elif escolha == 2: 
#         temp_digitada = float(input("Digite o valor a ser convertido:\n")) 
#         resultado = f"\nResultado: conversores(temp_digitada) {fahrenheit_celcius:.2f} °C\n"
#         return resultado
#     else: 
#         print("\nOpção não encontrada!\n")

from convert_c_f import celcius_fahrenheit
from convert_f_c import fahrenheit_celcius

def conversor(escolha, temp_digitada):
    if escolha == 1: 
        temp_digitada = float(input("Digite o valor a ser convertido:\n")) 
        resultado = celcius_fahrenheit(temp_digitada) 
        return resultado 
    elif escolha == 2: 
        temp_digitada = float(input("Digite o valor a ser convertido:\n")) 
        resultado = fahrenheit_celcius(temp_digitada)
        return resultado
    else: 
        print("\nOpção não encontrada!\n")