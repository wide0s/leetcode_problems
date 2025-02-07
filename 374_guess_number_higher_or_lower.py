# We are playing the Guess Game. The game is as follows:
# I pick a number from 1 to n. You have to guess which
# number I picked. Every time you guess wrong, I will tell
# you whether the number I picked is higher or lower than
# your guess.
#
# You call a pre-defined API int guess(int num), which
# returns three possible results:
#
#   -1: Your guess is higher than the number I picked 
#       (i.e. num > pick).
#    1: Your guess is lower than the number I picked 
#       (i.e. num < pick).
#    0: your guess is equal to the number I picked
#       (i.e. num == pick).
#
# Return the number that I picked.
#
# Constraints:
#  1 <= n <= 2^31 - 1
#  1 <= pick <= n

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo, hi = 1, n
        while lo < hi:
            mid = (hi + lo) // 2
            if guess(mid) > 0:
                lo = mid + 1
            else:
                hi = mid
        return lo

vectors = [
        10, 6,
        1, 1,
        2, 1
        ]

_picked = 1
def guess(hypothesis):
    return -1 if hypothesis > _picked else \
            1 if hypothesis < _picked else \
            0

for i in range(0, len(vectors), 2):
    n = vectors[i]
    print(n)
    _picked = vectors[i+1]
    returned = Solution().guessNumber(n)
    assert _picked == returned, f'for {n} expected {_picked}, but returned {returned}!'
