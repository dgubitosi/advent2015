
target = 36000000
i = 1
while True:
    t = 0
    for j in range(1, i):
        if i % j == 0: t += j*10
    if i % 1000 == 0: print(i, t)
    if t >= target: break
    i += 1

