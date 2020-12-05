
import sys
import itertools

def getmax():
    max = 0
    path = None
    perms = list(itertools.permutations(edges))
    for p in perms:
        distance = 0
        for i in range(1, len(p)):
            distance += edges[p[i-1]][p[i]]
            distance += edges[p[i]][p[i-1]]
        distance += edges[p[0]][p[-1]]
        distance += edges[p[-1]][p[0]]
        if distance > max:
            max = distance
            path = p
        print(p, distance)
    return max, path

edges = dict()
with open(sys.argv[1]) as f:
    for line in f:
        array = line[:-2].split()
        a = array[0]
        z = array[-1]
        d = int(array[3])
        if array[2] == 'lose':
            d *= -1
        edges.setdefault(a, {})
        edges[a].setdefault(z, d)

# prior to adding me
before = getmax()

# add me
me = 'me'
guests = set()
for e in edges:
    guests.add(e)
    edges[e].setdefault(me, 0)
edges[me] = dict()
for g in guests:
    edges[me].setdefault(g, 0)
after = getmax()

print()
print(before[1], before[0])
print(after[1], after[0])

change = after[0] - before[0]
print(change)
