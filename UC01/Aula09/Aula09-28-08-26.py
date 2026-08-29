#CÓDIGOS DESENVOLVIDOS EM AULA

#SORTEIO DE NUMEROS

def sorteiame ():
    '''
    Algoritmo escolhe e retorna um número inteiro aleatório entre o intervalo definido
    '''
    import random #para que minha função funcione independente do arquivo MAIN, eu posso definir o modulo dentro da função.
    numero_random = random.randint(1,30)
    return numero_random

