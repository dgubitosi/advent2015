
real_sue = dict()
with open("test.txt") as f:
    for line in f:
        t, n = line.strip().split(':')
        real_sue.setdefault(t, n)

with open("input.txt") as f:
    for line in f:
        sue, line = line.strip().split(':', 1)
        sue = sue.strip().split()[-1]
        array = line.strip().split(',')
        match = True
        for a in array:
            t, n = a.strip().split(':')
            if t in real_sue:
                # n should be more
                if t in [ 'cats', 'trees' ] and n <= real_sue[t]:
                    match = False
                    break
                # n should be less
                if t in [ 'pomeranians', 'goldfish' ] and n >= real_sue[t]:
                    match = False
                    break
                if t not in [ 'cats', 'trees', 'pomeranians', 'goldfish' ] and real_sue[t] != n:
                    match = False
                    break
        if match == True:
            print(sue)
