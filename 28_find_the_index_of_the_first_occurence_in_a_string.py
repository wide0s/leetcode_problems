# Given two strings needle and haystack, return the index of the first
# occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution(object):
    def find(self, haystack, needle):
        if len(haystack) < len(needle):
            return -1
        for i in range(0, len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return self.find(haystack, needle)

vectors = [
    'hello', 'll', 2,
    'sadbutsad', 'sad', 0,
    'leetcode', 'leeto', -1,
]

for i in range(0, len(vectors), 3):
    haystack = vectors[i]
    needle = vectors[i + 1]
    expected = vectors[i + 2]
    print(f'{haystack} {needle} {expected}')
    returned = Solution().strStr(haystack, needle)
    assert expected == returned, f'for haystack = {haystack} needle = {needle} expected {expected}, returned {returned}!'
