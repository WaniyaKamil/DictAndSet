from primes_squares import squares_generator, primes_generator

evens = set(range(0, 50, 2))
print(evens)
odds = set(range(1, 50, 2))
print(odds)

primes = set(primes_generator(100))
print(primes)
squares = set(squares_generator(100))
print(squares)

# print(odds.difference(primes))

print(primes-odds)
print(odds-primes)