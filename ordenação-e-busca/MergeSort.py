#possui ordem O(n * log(n)), porém requer espaço adicional

def mergeSort(lista):
    if len(lista) > 1:
        midpoint = len(lista) // 2
        leftLista = lista[:midpoint]
        rightLista = lista[midpoint:]
        mergeSort(leftLista)
        mergeSort(rightLista)
        i, j, k = 0, 0, 0
        while i < len(leftLista) and j < len(rightLista):
            if leftLista[i] < rightLista[j]:
                lista[k] = leftLista[i]
                i += 1
                k += 1
            else:
                lista[k] = rightLista[j]
                j += 1
                k += 1
        while i < len(leftLista):
            lista[k] = leftLista[i]
            i += 1
            k += 1
        while j < len(rightLista):
            lista[k] = rightLista[j]
            j += 1
            k += 1


lista = [54,26,93,17,77,31,44,55,20]
mergeSort(lista)

print(lista)