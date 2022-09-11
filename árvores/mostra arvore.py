temp = 0
def mostra2(arvore, prefix):
    global temp
    if arvore.dado:
        print(temp*prefix + f'{arvore.dado}')
    for filho in arvore.filhos:
        temp += 1
        mostra2(filho, prefix)
        temp -= 1

def mostra(arvore, prefix):
    global temp
    if arvore.dado:
        print(temp*prefix + f'{arvore.dado}')
    for filho in arvore.filhos:
        temp += 1
        mostra2(filho, prefix)
        temp -= 1
    temp = 0