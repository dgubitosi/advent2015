
import sys
import json

def walk(obj):
   paths = []
   if isinstance(obj, dict):
      for k, v in obj.items():
         # dict keys are in the path as strings
         #p = "{}({})".format(type(k).__name__, str(k))
         p = str(k)
         paths.append([p])
         paths += [[p] + x for x in walk(v)]
   elif isinstance(obj, list):
      for i, v in enumerate(obj):
         # list indices are in the path as integers
         #p = "index({})".format(str(i))
         p = i
         paths.append([p])
         paths += [[p] + x for x in walk(v)]
   elif isinstance(obj, str) or isinstance(obj, int) or isinstance(obj, float):
      # leafs are identified with v={VALUE}
      p = "v={}".format(str(obj))
      paths.append([p])
   return paths

with open(sys.argv[1]) as f:
   j  = json.load(f)

# find all paths
paths = walk(j)

# find all red paths
red_paths = []
for p in paths:
   # find all red leafs
   if p[-1] == 'v=red':
      # determine parent type
      # integer is a list index
      # string is a dict key
      if isinstance(p[-2], str):
         red_paths.append(p[:-2])

# sort red paths by len
red_paths.sort(key=len)

total = 0
for p in paths:
   if not isinstance(p[-1], str): continue
   if not p[-1].startswith('v='): continue
   if not p[-1][-1].isdigit(): continue

   i = int(p[-1].split('=')[-1])
   red = False
   print("PATH",p)
   for r in red_paths:
      if p[0] != r[0]: continue
      print("   *", r)
      lr = len(r)
      if p[0:lr] == r:
         print(" RED", r)
         red = True
         break
   if not red:
      print("GOOD", p)
      total += i

print(total)