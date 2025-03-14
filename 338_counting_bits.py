# Given an integer n, return an array ans of length n + 1 such that
# for each i (0 <= i <= n), ans[i] is the number of 1's in the binary
# representation of i.
#
# Example:
#  Input: n = 2
#  Output: [0,1,1]
#   Explanation:
#    0 --> 0
#    1 --> 1
#    2 --> 10
#
#  0 - 0000 0000      0
#  1 - 0000 0001      1
#  2 - 0000 0010      1
#  3 - 0000 0011      2
#  4 - 0000 0100      1
#  5 - 0000 0101      2
#  6 - 0000 0110      2
#  7 - 0000 0111      3
#  8 - 0000 1000      1
#  9 - 0000 1001      2
# 10 - 0000 1010      2
# 11 - 0000 1011      3
# 12 - 0000 1100      2
# 13 - 0000 1101      3
# 14 - 0000 1110      3
# 15 - 0000 1111      4
# 16 - 0001 0000      1
# 17 - 0001 0001      2
# 18 - 0001 0010      2
# 19 - 0001 0011      3
# 20 - 0001 0100      2
# 21 - 0001 0101      3
# 22 - 0001 0110      3
# 23 - 0001 0111      4
# 24 - 0001 1000      2
# 25 - 0001 1001      3
# 26 - 0001 1010      3
# 27 - 0001 1011      4 
# 28 - 0001 1100      3 
# 29 - 0001 1101      4 
# 30 - 0001 1110      4 
# 31 - 0001 1111      5 
# 32 - 0010 0000      1
# 33 - 0010 0001      2
# 34 - 0010 0010      2
# 35 - 0010 0011      3
# 36 - 0010 0100      2

# uses this https://stackoverflow.com/questions/51387998/count-bits-1-on-an-integer-as-fast-as-gcc-builtin-popcountint
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        bitcount = [
                0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4,\
                1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,\
                1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,\
                2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,\
                1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,\
                2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,\
                2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,\
                3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,\
                1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,\
                2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,\
                2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,\
                3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,\
                2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,\
                3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,\
                3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,\
                4, 5, 5, 6, 5, 6, 6, 7, 5, 6, 6, 7, 6, 7, 7, 8
                ]

        def popcount(n):
            count = 0
            while n > 0:
                # count bits of each byte
                count += bitcount[n & 0xff]
                n >>= 8
            return count

        return [ popcount(i) for i in range(n + 1) ]

vectors = [
        0,  [0],
        1,  [0,1],
        2,  [0,1,1],
        5,  [0,1,1,2,1,2],
        6,  [0,1,1,2,1,2,2],
        31, [0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4,1,2,2,3,2,3,3,4,2,3,3,4,3,4,4,5],
        32, [0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4,1,2,2,3,2,3,3,4,2,3,3,4,3,4,4,5,1]
        ]

for i in range(0, len(vectors), 2):
    n = vectors[i]
    print(f'n={n}')
    expected = vectors[i+1]
    returned = Solution().countBits(n)
    assert expected == returned, f'for {n} expected {expected}, but returned {returned}!'
