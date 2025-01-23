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

assert Solution().strStr("hello", "ll") == 2
assert Solution().strStr("sadbutsad", "sad") == 0
assert Solution().strStr("leetcode", "leeto") == -1
