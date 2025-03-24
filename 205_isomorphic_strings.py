from collections import defaultdict
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        s2t = defaultdict(str)
        t2s = defaultdict(str)
        for i in range(len(s)):
            if s[i] in s2t:
                if s2t[s[i]] != t[i]:
                    return False
            elif t[i] in t2s:
                return False
            else:
                s2t[s[i]] = t[i]
                t2s[t[i]] = s[i]
        return True

vectors = [
        ['egg', 'add'], True,
        ['foo', 'bar'], False,
        ['paper', 'title'], True
        ]

for i in range(0, len(vectors), 2):
    params = vectors[i]
    expected = vectors[i + 1]
    print(f'{params} {expected}')
    returned = Solution().isIsomorphic(*params)
    assert expected == returned, f'for {params} expected {expected}, returned {returned}!'
