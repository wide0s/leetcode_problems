class Solution(object):
    # brute force, exeedes time limit for 9999999
    def bulbSwitchBruteForce(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        bulbs = [ 0 for _ in range(n) ]
        nums = 0
        for j in range(len(bulbs)):
            for i in range(j, len(bulbs), j + 1):
                bulbs[i] = 1 - bulbs[i]
        for i in range(len(bulbs)):
            if bulbs[i] != 0:
                nums += 1
        return nums

    cache = [1, 1]
    # quickest solution with caching, beats %100 (runtime)
    def bulbSwitch(self, n):
        if n == 0:
            return 0
        m = 1 if n < self.cache[0] else self.cache[1]
        while m * m <= n:
            m += 1
        self.cache[0], self.cache[1] = n, m - 1
        return m - 1


hm = dict()
for n in range(225):
    expected = Solution().bulbSwitchBruteForce(n)
    if expected in hm:
        hm[expected] += [n]
    else:
        hm[expected] = [n]
for key in hm:
    print(f'{key} {hm[key]}')
    actual = Solution().bulbSwitch(n)
    assert expected == actual, 'for {n} expected {expected}, returned {actual}' 
