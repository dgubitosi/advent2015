import numpy
import itertools

def prime_factors(n):
    for i in itertools.chain([2], itertools.count(3, 2)):
        if n <= 1:
            break
        while n % i == 0:
            n //= i
            yield i

target = 36000000
last = 0
i = 6
while True:
    # multiples of six seem to have the most factors
    house = i
    factors = list(prime_factors(house))

    n = set()
    for j in range(1, len(factors)):
        l = list(itertools.combinations(factors, j))
        #print(house, j, l)
        for k in itertools.combinations(factors, j):
            n.add(numpy.prod(k)*10)
    presents = sum(list(n))
    print(house, presents)
    if presents > target:
        i /= 2
        i *= 1.5
        i = int(i)
    if presents < target:
        i *= 2

