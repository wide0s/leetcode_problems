# You are given a string s. The score of a string is
# defined as the sum of the absolute difference between
# the ASCII values of adjacent characters.
#
# Return the score of s.
#
# Constraints:
#  2 <= s.length <= 100
#  s consists only of lowercase English letters.

class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        assert len(s) > 1
        score = 0
        for index in range(0, len(s) - 1):
            score += abs(ord(s[index + 1]) - ord(s[index]))
        return score

vectors = [
        "hello", 13,
        "zaz", 50
        ]

for i in range(0, len(vectors), 2):
    s = vectors[i]
    print(f'{s}')
    expected = vectors[i+1]
    returned = Solution().scoreOfString(s)
    assert expected == returned, f'for \'{s}\' expected {expected}, but returned {returned}!'
