#Ordenacao_python_ver1.2 
#estudno de ordnação por Bubble_sort  
numeros = [3, 2, 10, 13, 4, 20]

print(f"a lista inicial é\n: {numeros}\n")

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


bubble_sort(numeros)
print(f"a lista ordenada agora é\n: {numeros}")
