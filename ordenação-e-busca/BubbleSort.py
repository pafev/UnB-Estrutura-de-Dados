#Possui ordem O(n**2)

def bubbleSort(lista):
    passnum = len(lista) - 1
    while passnum > 0:
        for i in range(passnum):
            if (lista[i] // 1) > (lista[i + 1] // 1):
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
        passnum -= 1

def shortBubbleSort(lista):
    passnum = len(lista) - 1
    ordenado = False
    while passnum > 0 and not ordenado:
        ordenado = True
        for i in range(passnum):
            if lista[i] == lista[i + 1]:
                ordenado = False
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
        passnum -= 1


lista = [20,30.1,30.2,90,50,60,70,80,100,110]
bubbleSort(lista)
#shortBubbleSort(lista)

print(lista)