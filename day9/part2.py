
import sys
import itertools

edges = dict()
with open(sys.argv[1]) as f:
    for line in f:
        array = line.strip().split()
        a = array[0]
        z = array[2]
        d = int(array[-1])
        edges.setdefault(a, {})
        edges[a].setdefault(z, d)
        edges.setdefault(z, {})
        edges[z].setdefault(a, d)

min = float('inf')
max = -1
minpath = None
maxpath = None
perms = list(itertools.permutations(edges))
for p in perms:
    distance = 0 
    for i in range(1, len(p)):
       distance += edges[p[i-1]][p[i]]
    if distance < min:
       min = distance
       minpath = p
    if distance > max:
       max = distance
       maxpath = p
    print(p, distance)
print(minpath, min)
print(maxpath, max)
