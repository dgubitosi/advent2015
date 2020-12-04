
import sys

floor = 0
with open(sys.argv[1]) as f:
    while True:
        c = f.read(1)
        if not c: break
        if c == "(": floor += 1
        if c == ")": floor -= 1
print(floor)
