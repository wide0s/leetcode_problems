# Given two strings s and t, return true
# if t is an  anagram of s, and false 
# otherwise.
#
# Constraints:
#  1 <= s.length, t.length <= 5 * 104
#  s and t consist of lowercase English
#  letters.

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        freqs = [0] * 26
        for ch1, ch2 in zip(s,t):
            freqs[ord(ch1) - ord('a')] += 1
            freqs[ord(ch2) - ord('a')] -= 1
        for i in range(len(freqs)):
            if freqs[i] != 0:
                return False
        # 25ms beats 37%
        return True

vectors = [
        "ggii", "eekk", False,
        "rat", "car", False,
        "anagram", "margana", True,
        "anagram", "gnaarma", True,
        "anagram", "nagaram", True
        ]

for i in range(0, len(vectors), 3):
    s = vectors[i]
    t = vectors[i+1]
    print(f'{s} {t}')
    expected = vectors[i+2]
    returned = Solution().isAnagram(s, t)
    assert expected == returned, f'isAnagram(\'{s}\',\'{t}\') = {expected}, but returned {returned}!'
