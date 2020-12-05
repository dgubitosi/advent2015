
import sys

reindeer = dict()
seconds = 2503
with open(sys.argv[1]) as f:
    for line in f:
        array = line.split()
        name = array[0]
        speed = int(array[3])
        duration = int(array[6])
        rest = int(array[-2])
        interval = duration + rest
        intervals = seconds // interval
        distance = intervals * speed * duration
        remainder = seconds % interval
        distance += speed * min([duration, remainder])
        reindeer.setdefault(name, distance)

for r in sorted(reindeer, key=reindeer.get, reverse=True):
    print(r, reindeer[r])