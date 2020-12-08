
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
            try:
                if real_sue[t] != n:
                    match = False
                    break
            except:
                pass
        if match == True:
            print(sue)
