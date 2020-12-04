
import sys

pos = [ [ 0,0 ], [ 0,0 ] ]
x = 0
y = 1

visits = { (0,0): 1 }
i = 0
with open(sys.argv[1]) as f:
    while True:
        c = f.read(1)
        if not c: break
        j = i % 2
        p = pos[j]
        if c == ">": p[x] += 1
        if c == "<": p[x] -= 1
        if c == "^": p[y] += 1
        if c == "v": p[y] -= 1
        visits.setdefault(tuple(p), 0)
        visits[tuple(p)] += 1
        i += 1
print(len(visits))
