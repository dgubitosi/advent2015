import sys

def twos(s):
    for i in range(0, len(s)):
        two = s[i:i+2]
        if two in s[i+2:]: return True
    return False

def threes(s):
    for i in range(2, len(s)):
        if s[i] == s[i-2]: return True
    return False

nice = []
with open(sys.argv[1]) as f:
    for line in f:
        s = line.strip()
        if not twos(s): continue
        if not threes(s): continue
        nice.append(s)
print(len(nice))
