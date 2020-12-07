
import sys

def calculate(ratio):
    score = 1
    properties = dict()
    for p in propertySet:
        value = 0
        for index, ingredient in enumerate(ingredients):
            value += ratio[index] * ingredientProperties[ingredient][p]
        if value < 0: value = 0
        properties.setdefault(p, value)
        if p != 'calories':
            score *= value
    properties['score'] = score
    return properties

ingredientSet = set()
ingredientProperties = dict()
propertySet = set()
with open(sys.argv[1]) as f:
    for line in f:
        i, p = line.strip().split(':')
        ingredientSet.add(i)
        properties = dict()
        array = p.split(',')
        for a in array:
            prop, value = a.strip().split()
            properties.setdefault(prop, int(value))
            propertySet.add(prop)
        ingredientProperties.setdefault(i, {})
        ingredientProperties[i] = properties

ingredients = sorted(list(ingredientSet))
cookies = dict()
best = 0
r = None

# stars and bars problem
n = 100
p = 4
s = [ 1 ] * n
for i in range(1, len(s)-p-1):
    for j in range(i+1, len(s)-p-1):
        for k in range(j+1, len(s)-p-1):
            ratio = tuple([ len(s[0:i]), len(s[i:j]), len(s[j:k]), len(s[k:]) ])
            cookies.setdefault(ratio, dict())
            cookies[ratio] = calculate(ratio)
            if cookies[ratio]['score'] > best:
                best = cookies[ratio]['score']
                r = ratio

print(r, cookies[r])
for i, x in enumerate(r):
    ingredient = ingredients[i]
    print('{} x {} {}'.format(x, ingredient, ingredientProperties[ingredient]))