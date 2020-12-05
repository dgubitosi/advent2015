
def increment(p):
    pos = 0
    for i in range(len(p)):
        if i > pos:
            break
        if i == pos:
            p[i] += 1
            if p[i] > 25:
                p[i] = 0
                pos += 1
    return p

def convert(p):
   s = []
   i = len(p)-1
   while i >= 0:
       s.append(chr(ord('a')+p[i]))
       i -= 1
   return ''.join(s)

def bad(s):
    if 'i' in s or 'o' in s or 'l' in s: return True
    return False

def three(s):
    for i in range(len(s)-2):
        n = ord(s[i])
        if s[i+1] == chr(n+1) and s[i+2] == chr(n+2): return True
    return False

def two(s):
    pairs = set()
    for i in range(len(s)-1):
        if s[i] == s[i+1]: pairs.add(tuple([s[i],s[i+1]]))
    if len(pairs) > 1: return True
    return False

def valid(s):
    if bad(s): return False
    if not three(s): return False
    if not two(s): return False
    return True

p  = 'hepxcrrq'
pp = [ (ord(x) - ord('a')) for x in p ]
pp.reverse()
pp = increment(pp)

while True:
    s = convert(pp)
    print(s, pp)
    if valid(s):
        print(s)
        break
    pp = increment(pp)
