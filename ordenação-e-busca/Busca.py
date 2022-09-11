def sequentialSearch(lista, item): 
    #Possui complexidade de ordem O(n)
    for _ in lista:
        if _ == item:
            return True
    return False

def binarySearch(lista, item):
    #Possui complexidade O(log(n)) no pior caso, porém só funciona para listas ordenadas
    midpoint = len(lista) // 2
    if not len(lista):
        return False
    elif lista[midpoint] != item and len(lista) == 1:
        return False
    elif lista[midpoint] == item:
        return True
    elif lista[midpoint] <  item:
        return binarySearch(lista[midpoint + 1:], item)
    else:
        return binarySearch(lista[:midpoint], item)

listaTeste = [13,17,28,37,54,72,87]