# ref 264_ugly_number.py
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ugly_numbers = [1]
        indices = [0] * len(primes)
        cands = [0] * len(indices)
        while len(ugly_numbers) < n:
            for j in range(len(indices)):
                cands[j] = ugly_numbers[indices[j]] * primes[j]
            ugly = min(cands)
            ugly_numbers.append(ugly)

            for j in range(len(indices)):
                if ugly == cands[j]:
                    indices[j] += 1
        return ugly_numbers[-1]

vectors = [
    [[12, [2,7,13,19]], 32],
    [[1, [2,3,5]], 1]
]

for vector in vectors:
    params = vector[0]
    expected = vector[1]
    print(f'{params[0]}th super ugly number is {expected}')
    returned = Solution().nthSuperUglyNumber(*params)
    assert expected == returned, f'for {params} expected {expected}, returned {returned}!'