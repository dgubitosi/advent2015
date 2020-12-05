
import sys

try:
    n = sys.argv[1]
except:
    n = str(3113322113)

for i in range(40):
    prev = n
    n = ''
    j = 0
    while j < len(prev):
        char = prev[j]
        k = j + 1
        while k < len(prev) and prev[k] == prev[j]:
            k += 1
        count = k - j
        n += str(count) + char
        j += count
    #print(i, prev, n)
print(len(n))
