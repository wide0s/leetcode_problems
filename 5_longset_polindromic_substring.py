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

vectors = [
        'a', 'a',
        'bb', 'bb',
        'abacab', 'bacab',
        'cbbd', 'bb',
        'wowbababcbabaxy', 'ababcbaba',
        'cccccccccccccccccccc', 'cccccccccccccccccccc'
        ]

for i in range(0, len(vectors), 2):
    s = vectors[i]
    expected = vectors[i + 1]
    print(f'{s} {expected}')
    returned = Solution().longestPalindrome(s)
    assert expected == returned, f'for {s} expected {expected}, returned {returned}!'
