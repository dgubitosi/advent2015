
import sys
from itertools import combinations 

total = 0
with open(sys.argv[1]) as f:
    for line in f:
        d = sorted([ int(x) for x in line.strip().split('x') ])
        #print(d)
        sides = list(combinations(d, 2))
        area = 0
        for i,s in enumerate(sides):
            a = s[0]*s[1]
            if i == 0:
                a *= 3
            else:
                a *= 2
            print(i,s,a)
            area += a
        print(d, area)
        total += area
print(total)
