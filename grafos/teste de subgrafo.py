isSub = True

edges1 = []
numVert1 = int(input())
count = 0
while count < numVert1:
    id, A, *verts = map(int, input().split())
    for vert in verts:
        temp = [id, vert]
        temp.sort()
        if temp not in edges1:
            edges1.append(temp)
    count += 1
input()
edges2 = []
numVert2 = int(input())
count = 0
while count < numVert2:
    id, A, *verts = map(int, input().split())
    for vert in verts:
        temp = [id, vert]
        temp.sort()
        if temp not in edges1:
            isSub = False
            break
    count += 1

if isSub:
    print('Sub-sub!')
else:
    print('Ue? Ue? Ue?')