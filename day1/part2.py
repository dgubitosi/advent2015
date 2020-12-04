
import sys

floor = 0
pos = 0
with open(sys.argv[1]) as f:
    while True:
        c = f.read(1)
        if not c: break
        pos += 1
        if c == "(": floor += 1
        if c == ")": floor -= 1
        if floor == -1: break
print(pos, floor)
