def fib(n):
    sqroot = 5 ** 0.5
    phi = (sqroot + 1) / 2
    return int(phi ** n / sqroot + 0.5)

mile_distances = [1.0, 6.5, 17.4, 2.4, 9.2]

km_dist = list(map(lambda x: x * 1.6, mile_distances))
print(km_dist)
