
import sys

reindeer = dict()
with open(sys.argv[1]) as f:
    for line in f:
        array = line.split()
        name = array[0]
        speed = int(array[3])
        duration = int(array[6])
        rest = int(array[-2])
        d = {
            "speed": speed,
            "duration": duration,
            "rest": rest,
            "distance": 0,
            "score": 0
        }
        reindeer.setdefault(name, {})
        reindeer[name] = d

try:
    seconds = int(sys.argv[2])
except:
    seconds = 2503
lead = 0
for s in range(1, seconds+1):
    for r in reindeer:
        print(s, r, reindeer[r])
        speed = reindeer[r]['speed']
        duration = reindeer[r]['duration']
        rest = reindeer[r]['rest']
        interval = duration + rest
        intervals, remainder = divmod(s, interval)
        reindeer[r]['distance'] = intervals * speed * duration
        reindeer[r]['distance'] += speed * min([remainder, duration])

    # more than one reindeer can earn a point if they are tied in the lead
    for r in sorted(reindeer, key=lambda k: reindeer[k]['distance'], reverse=True):
        if reindeer[r]['distance'] >= lead:
            lead = reindeer[r]['distance']
            reindeer[r]['score'] += 1
        else:
            break

for r in sorted(reindeer, key=lambda k: reindeer[k]['score'], reverse=True):
    print(r, reindeer[r])

