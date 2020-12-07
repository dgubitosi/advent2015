
import sys

ingredients = dict()
with open(sys.argv[1]) as f:
    for line in f:
        i, p = line.strip().split(':')
        properties = dict()
        array = p.split(',')
        for a in array:
            property, value = a.strip().split()
            properties.setdefault(property, int(value))
        ingredients.setdefault(i, {})
        ingredients[i] = properties

# stars and bars problem
n = 100
p = 4
s = [ 1 ] * n
ratios = []
for i in range(1, len(s)-p-1):
    for j in range(i+1, len(s)-p-1):
        for k in range(j+1, len(s)-p-1):
            ratios.append([ len(s[0:i]), len(s[i:j]), len(s[j:k]), len(s[k:]) ])

l = list(ingredients)
scores = dict()
for r in ratios:
    score = 1
    properties = { 'capacity':0, 'durability':0, 'flavor':0, 'texture':0 }
    for p in properties:
        for index, ingredient in enumerate(l):
            properties[p] += r[index] * ingredients[ingredient][p]
        if properties[p] < 0: properties[p] = 0
        score *= properties[p]
    t = tuple(r)
    scores.setdefault(t, dict())
    scores[t]['properties'] = properties
    scores[t]['ingredients'] = l
    scores[t]['score'] = score
    #print(t, properties, score)

for i in ingredients:
    print(i, ingredients[i])
for s in sorted(scores, key=lambda k: scores[k]['score'], reverse=True):
    print(s, scores[s])
    break

