class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s2 = [c.lower() for c in s if c.isalnum()]
        return s2 == s2[::-1]

vectors = [
        "", True,
        "A man, a plan, a canal: Panama", True,
        "race a car", False,
        "9P", False,
        " ", True
        ]

for i in range(0, len(vectors), 2):
    s = vectors[i]
    print(f'\'{s}\'')
    expected = vectors[i + 1]
    returned = Solution().isPalindrome(s)
    assert expected == returned, f'for \'{s}\' expected {expected}, but returned {returned}!'
