
import sys

pos = [ 0,0 ]
x = 0
y = 1
visits = { tuple(pos): 1 }
with open(sys.argv[1]) as f:
    while True:
        c = f.read(1)
        if not c: break
        if c == ">": pos[x] += 1
        if c == "<": pos[x] -= 1
        if c == "^": pos[y] += 1
        if c == "v": pos[y] -= 1
        visits.setdefault(tuple(pos), 0)
        visits[tuple(pos)] += 1
print(len(visits))
