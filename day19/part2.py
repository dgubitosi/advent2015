
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

for r in replacements:
    print(r, sorted(replacements[r], key=lambda x: (len(x),x)))
print()
print(target)
print()

# work backwards from target, reducing the instances of {foo}Rn{bar}Ar ??

import re
for iter in re.finditer(r'Rn[^Rn]+?Ar', target):
    start = iter.start() - 1
    if target[start].islower(): start -= 1
    end = iter.end()
    print(start,end,target[start:end])

'''
# lol i didn't think brute force would work
toSolve = [{'e': 0}]
solutions = []
while toSolve:
    t = toSolve.pop(0)
    solutions.append(t)
    word = list(t.keys())[-1]
    steps = t[word]
    print(len(solutions), steps, word)
    for i in range(len(word)):
        check = [ word[i] ]
        if i > 0: check.append( word[i-1:i+1] )
        for c in check:
            if not c in replacements: continue
            for r in replacements[c]:
                t = word[0:i+1-len(c)] + r + word[i+1:]
                if t == target:
                    print(steps + 1)
                    break
                else:
                    toSolve.append({t: steps + 1})
'''