from algorithms import bisection, gcd, prod

# bisection
for i in range(20):
    a = [ x for x in range(i) ]
    for j, target in enumerate(a):
        assert bisection(a, target) == j
    assert bisection(a, -1) == -1
    assert bisection(a, len(a)) == -1

vectors = [
        [1, 2, 3, 4], 0, 3, 4, -1,
        [1, 2, 3, 4], 1, 4, 1, -1,
        [1, 2, 3, 4], 2, None, 3, 2,
        [1, 2, 3, 4], 1, 4, 3, 2
]

for i in range(0, len(vectors), 5):
    a = vectors[i]
    left = vectors[i + 1]
    right = vectors[i + 2]
    target = vectors[i + 3]
    expected = vectors[i + 4]
    returned = bisection(a, target, left, right)
    assert returned == expected, f'for {a} and target {target} in boundaries [{left},{right}] expected index {expected}, returned {returned}!'

# prod
vectors = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]
expected = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 0]
for i in range(len(vectors)):
    p = prod(vectors[0:i + 1])
    assert p == expected[i], f'for {vectors[0:i + 1]} expected {expected[i]}, but returned {p}'

# gcd
assert gcd(0, 123456789) == 123456789
assert gcd(987654321, 0) == 987654321

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
p = prod(primes)
for a, b in zip(primes, primes[::-1]):
    r = gcd(a, b)
    assert r == 1, f'gcd({a},{b}) == 1, but returned {r}!'
    r2 = gcd(b, a)
    assert r == r2, f'{r} = gcd({a},{b}) != gcd({b},{a}) = {r2}!'
    r = gcd(a, p)
    assert r == a, f'gcd({a}, {p}) == {a}, but returned {p}'

i = 0
for a in range(2, 10):
    i += 1
    r = gcd(a, pow(a, i))
    assert r == a, f'gcd({a},{a}^{i}) == {a}, but returned {r}'
