# Given two strings s and t, return true if s is a subsequence of t,
# or false otherwise.
#
# A subsequence of a string is a new string that is formed from the
# original string by deleting some (can be none) of the characters 
# without disturbing the relative positions of the remaining characters.
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
#
# Example 1:
#  Input: s = "abc", t = "ahbgdc"
#  Output: true
#
# Example 2:
#  Input: s = "axc", t = "ahbgdc"
#  Output: false
#
# Constraints:
#  0 <= s.length <= 100
#  0 <= t.length <= 104
#  s and t consist only of lowercase English letters.

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        found = 0
        if len(s) > 0:
            index = 0
            while found < len(s) and index < len(t):
                if t[index] == s[found]:
                    found += 1
                index += 1
        return found == len(s)

vectors = [
        "", "a", True,
        "a", "", False,
        "", "ahbgdc", True,
        "abc", "ahbgdc", True,
        "axc", "ahbgdc", False
        ]

for i in range(0, len(vectors), 3):
    s = vectors[i]
    t = vectors[i+1]
    expected = vectors[i+2]
    returned = Solution().isSubsequence(s, t)
    assert expected == returned, f'for s \'{s}\' and t \'{t}\' expected {expected}, returned {returned}!'
