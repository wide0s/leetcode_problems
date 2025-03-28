# n passengers board an airplane with exactly n seats.
# The first passenger has lost the ticket and picks a
# seat randomly. But after that, the rest of the passengers
# will:
#
#  Take their own seat if it is still available, and
#  Pick other seats randomly when they find their seat occupied
#
# Return the probability that the nth person gets his own seat.
#
# Example 1:
#  Input: n = 1
#  Output: 1.00000
#  Explanation: The first person can only get the first seat.
# Example 2:
#  Input: n = 2
#  Output: 0.50000
#  Explanation: The second person has a probability of 0.5 to get
#    the second seat (when first person gets the first seat).
#
# Constraints:
#  1 <= n <= 105
class Solution(object):
    def nthPersonGetsNthSeat(self, n):
        """
        :type n: int
        :rtype: float
        """
        return 1 if n == 1 else 0.5

vectors = [
        1, 1,
        2, 0.5
        ]

for i in range(0, len(vectors), 2):
    seats = vectors[i]
    expected = vectors[i+1]
    print(f'{seats} {expected}')
    returned = Solution().nthPersonGetsNthSeat(seats)
    assert expected == returned, f'for {seats} seats expected probability is {expected}, but returned {returned}!'
