
import sys

size = 100
lights = [[ False for x in range(size)] for y in range(size)]

with open(sys.argv[1]) as f:
    row = 0
    for line in f:
        for i, c in enumerate(line.strip()):
            if c == '#': lights[row][i] = True
        row += 1

def cornersOn():
    global lights
    lights[0][0] = True
    lights[0][size-1] = True
    lights[size-1][0] = True
    lights[size-1][size-1] = True

def countOn(doPrint=False):
    on = 0
    for i in range(size):
        row = []
        for j in range(size):
            c = '.'
            if lights[i][j]:
                on += 1
                c = '#'
            if doPrint:
                row.append(c)
        print(''.join(row))
    return on

cornersOn()
steps = 100
for s in range(steps):
    temp = [[ False for x in range(size)] for y in range(size)]
    n = countOn(True)
    print(s, n)
    for i in range(size):
        for j in range(size):
            on = 0
            for m in [i-1, i, i+1]:
                for n in [j-1, j, j+1]:
                    #print(tuple([i,j]),tuple([m,n]))
                    if m == i and n == j: continue
                    if m < 0 or m >= size or n < 0 or n >= size: continue
                    if lights[m][n]: on += 1
            state = lights[i][j]
            new_state = state
            if state and (on < 2 or on > 3):
                state = False
            if not state and on == 3:
                state = True
            temp[i][j] = state
    lights = temp
    cornersOn()

n = countOn(True)
print(s, n)
