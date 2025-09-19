# ref https://webrewrite.com/find-nth-ugly-number/
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly_numbers = [1]
        index2, index3, index5 = 0, 0, 0
        while len(ugly_numbers) < n:
            cand2 = ugly_numbers[index2] * 2
            cand3 = ugly_numbers[index3] * 3
            cand5 = ugly_numbers[index5] * 5
            ugly = min(cand2, cand3, cand5)
            ugly_numbers.append(ugly)
            if ugly == cand2:
                index2 += 1
            if ugly == cand3:
                index3 += 1
            if ugly == cand5:
                index5 += 1
        return ugly_numbers[-1]

vectors = [
    [1, 1],
    [2, 2],
    [3, 3],
    [4, 4],
    [5, 5],
    [6, 6],
    [7, 8],
    [8, 9],
    [9, 10],
    [10, 12],
    [250, 38880],
    [1000, 51200000],
    [1690, 2123366400]
]

for vector in vectors:
    params = vector[0]
    expected = vector[1]
    print(f'{params}th ugly number is {expected}')
    returned = Solution().nthUglyNumber(params)
    assert expected == returned, f'for {params} expected {expected}, returned {returned}!'