# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
#
# Constraints:
#  1 <= strs.length <= 200
#  0 <= strs[i].length <= 200
#  strs[i] consists of only lowercase English letters if it is non-empty.

class Solution(object):
    def longestCommonPrefixMy(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]
        ss = sorted(strs, key=lambda s: len(s))
        stop = False
        prefix = ''
        for i, ch in enumerate(ss[0]):
            for s in ss[1:]:
                if s[i] != ch:
                    stop = True
                    break
            if stop:
                break
            print(ch)
            prefix += ch
        print(prefix)
        return prefix

    def longestCommonPrefixFast(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]
        ss = sorted(strs)
        stop = False
        prefix = ''
        for i, ch in enumerate(ss[0]):
            if ss[-1][i] != ch:
                break
            prefix += ch
        return prefix

vectors = [
    ['flower','flow','flight'], 'fl',
]

for i in range(0, len(vectors), 2):
    strs = vectors[i]
    expected = vectors[i + 1]
    print(f'{strs} {expected}')
    returned = Solution().longestCommonPrefixMy(strs)
    assert expected == returned, f'for strs = {strs} expected {expected}, returned {returned}!'
