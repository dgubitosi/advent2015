
import re
import sys

with open(sys.argv[1]) as f:
    data = f.read()

numbers = re.findall('[^-0-9]([-0-9]+)', data)

total = 0
for n in numbers:
   total += int(n)
print(total)
