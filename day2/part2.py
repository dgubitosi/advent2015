
import sys
from itertools import combinations 

total = 0
with open(sys.argv[1]) as f:
    for line in f:
        d = sorted([ int(x) for x in line.strip().split('x') ])
        l = d[0]*2 + d[1]*2 + d[0]*d[1]*d[2]
        print(d, l)
        total += l 
print(total)
