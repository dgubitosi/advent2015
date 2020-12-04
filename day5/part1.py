import sys

def threeVowels(s):
    vowels = 'aeiou'
    count = 0
    for c in s:
        if c in vowels: count += 1
        if count > 2: return True
    return False

def doubleLetters(s):
    for i in range(1, len(s)):
        if s[i] == s[i-1]: return True
    return False

def badPairs(s):
    bad = [ 'ab', 'cd', 'pq', 'xy' ]
    for b in bad:
        if b in s: return True
    return False

nice = []
with open(sys.argv[1]) as f:
    for line in f:
        s = line.strip()
        if not threeVowels(s): continue
        if not doubleLetters(s): continue
        if badPairs(s): continue
        nice.append(s)
print(len(nice))
