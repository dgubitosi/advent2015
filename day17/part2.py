
# https://stackoverflow.com/questions/4632322/finding-all-possible-combinations-of-numbers-to-reach-a-given-sum
def subset_sum(numbers, target, partial=[], results=[]):
    s = sum(partial)
    if s == target: 
        results.append(len(partial))
        return
    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining, target, partial + [n], results)
    return results

containers = list() 
with open("input.txt") as f:
    containers = [ int(x.strip()) for x in f.readlines() ]

s = subset_sum(containers, 150)
d = dict((i, s.count(i)) for i in s)
print(list(sorted(d.items()))[0])

