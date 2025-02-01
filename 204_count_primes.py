class Solution(object):
    # too slow for leetcode :(
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # too slow for leetcode :(
        def erathosthenesSlow(n):
            sieve = [True] * n
            primes = []
            for p in range(2, n):
                if sieve[p]:
                    primes.append(p)
                    for i in range(p*p, n, p):
                        sieve[i] = False
            return primes

        def erathosthenes(n):
            prime = [True for i in range(n + 1)]
            p = 2
            while (p * p < n):
                if prime[p] == True:
                    for i in range(p * p, n + 1, p):
                        prime[i] = False
                p += 1
            count = 0
            for p in range(2, n):
                if prime[p]:
                    count += 1
            return count

        return erathosthenes(n)

vectors = [
        35, 11,
        12, 5,
        10, 4,
        0, 0,
        1, 0,
        2, 0,
        2000, 303,
        20000, 2262,
        200000, 17984,
        2000000, 148933,
        20000000, 1270607
        ]

for i in range(0, len(vectors), 2):
    result = Solution().countPrimes(vectors[i])
    assert result == vectors[i + 1], f'there are {vectors[i+1]} primes less than {vectors[i]}, but returned {result}!'
