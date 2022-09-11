#Possui ordem O(n**2)

def insertionSort(lista):
    for i in range(1, len(lista)):
        currentValue = lista[i]
        position = i
        while position > 0 and currentValue < lista[position - 1]:
            lista[position] = lista[position - 1]
            position -= 1
        lista[position] = currentValue

#lista = [54,26,93,17,77,31,44,55,20]
#insertionSort(lista)

#print(lista)