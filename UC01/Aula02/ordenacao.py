#Ordenacao_python_ver1.0  
n1 = float(input("Digite o 1° número: "))  
n2 = float(input("Digite o 2° Número: "))  
n3 = float(input("Digite o 3° Número: "))  

if n1 > n2:  
    aux = n1  
    n1 = n2  
    n2 = aux   
if n2 > n3: 
    aux = n2  
    n2 = n3  
    n3 = aux   
if n1 > n2:  
 aux = n1  
 n1 = n2  
 n2 = aux 

print(f"Números ordenados: {n1}, {n2}, {n3}") 