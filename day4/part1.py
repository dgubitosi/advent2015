
import sys
import hashlib 

input = sys.argv[1]
i = 0
while True:
    t = input + str(i)
    md5 = hashlib.md5(t.encode('ascii')).hexdigest()
    if md5.startswith('0'*5):
        print(i, t, md5)
        break
    i += 1
