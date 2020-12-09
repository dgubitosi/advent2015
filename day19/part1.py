
replacements = dict()
target = None
with open("input.txt") as f:
    for line in f:
        array = line.strip().split(' => ')
        if len(array) == 1: 
            if array[0]: target = array[0]
        if len(array) == 2:
            src = array[0]
            dst = array[1]
            replacements.setdefault(src, [])
            replacements[src].append(dst)

'''
print(target)
for r in replacements:
    print(r, replacements[r])
'''

targets = set()
for i in range(len(target)):
    check = [ target[i] ]
    if i > 0: check.append( target[i-1:i+1] )
    for c in check:
        if not c in replacements: continue
        for r in replacements[c]:
            t = target[0:i+1-len(c)] + r + target[i+1:]
            targets.add(t)
print(len(targets))
