
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = s[0]
        for start in range(len(s)):
            if len(longest) >= len(s) - start:
                break
            for end in range(len(s) - 1, max(len(longest) - 1, start), -1):
                sub = s[start:end + 1]
                if sub == sub[::-1]:
                    if len(longest) <= len(sub):
                        longest = sub
                    break
        return longest

assert Solution().longestPalindrome('a') == 'a'
assert Solution().longestPalindrome('bb') == 'bb'
assert Solution().longestPalindrome("abacab") == "bacab"
assert Solution().longestPalindrome("cbbd") == "bb"
assert Solution().longestPalindrome("wowbababcbabaxy") == "ababcbaba"
assert Solution().longestPalindrome("cccccccccccccccccccc") == "cccccccccccccccccccc"
