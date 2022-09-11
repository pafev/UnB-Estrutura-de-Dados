n = int(input())
temCiclo = True
for i in range(n):
    id, A, *args = input().split()
    if int(A) == 0:
        temCiclo = False

if temCiclo:
    print('Hoje tem!')
else:
    print('... que ama ninguem.')