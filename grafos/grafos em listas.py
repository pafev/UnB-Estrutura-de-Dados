V, E, C = input().split()
V = int(V)
E = int(E)
graph = [[0 for j in range(V)] for i in range(V)]
if C == 'N':
    for aresta in range(E):
        X, Y, P = map(int, input().split())
        graph[X - 1][Y - 1] = P
        graph[Y - 1][X - 1] = P
elif C == 'D':
    for aresta in range(E):
        X, Y, P = map(int, input().split())
        graph[X - 1][Y - 1] = P

for linha in graph:
    for elemento in linha:
        print(f'{elemento:#4}', end ='')
    print()