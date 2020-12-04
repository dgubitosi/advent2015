
import re
import sys

size = 1000
lights = [[ 0 for x in range(size)] for y in range(size)] 

with open(sys.argv[1]) as f:
    for line in f:
        m = re.match('^(.*) ([0-9]+),([0-9]+) through ([0-9]+),([0-9]+)$', line)
        instruction = m.group(1)
        start = [ int(m.group(2)), int(m.group(3)) ]
        stop  = [ int(m.group(4)), int(m.group(5)) ]
        #print(instruction,start,stop)
        for y in range(start[1], stop[1]+1):
            for x in range(start[0], stop[0]+1):
                #print('{}({},{})={}'.format(instruction,x,y,lights[y][x]))
                if instruction == 'turn on':
                    lights[y][x] += 1
                    continue
                if instruction == 'turn off':
                    lights[y][x] -= 1
                    if lights[y][x] < 0: lights[y][x] = 0
                    continue
                if instruction == 'toggle':
                    lights[y][x] += 2

total = 0
for y in range(0, size):
    for x in range(0, size):
        total += lights[y][x]
print(total)
