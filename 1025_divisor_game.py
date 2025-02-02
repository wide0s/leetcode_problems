# Alice and Bob take turns playing a game, with Alice starting first.
# Initially, there is a number n on the chalkboard. On each player's
# turn, that player makes a move consisting of:
#
#  * Choosing any x with 0 < x < n and n % x == 0.
#
#  * Replacing the number n on the chalkboard with n - x.
#
# Also, if a player cannot make a move, they lose the game.
#
# Return true if and only if Alice wins the game, assuming both players play optimally.
#
# Constraints:
#
#  1 <= n <= 1000

class Solution(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 2 == 0

vectors = [
        2, True,
        3, False
        ]

for i in range(0, len(vectors), 2):
    number = vectors[i]
    print(number)
    expected = vectors[i + 1]
    returned = Solution().divisorGame(number)
    assert expected == returned, f'for {number} expected {expected}, returned {returned}'
