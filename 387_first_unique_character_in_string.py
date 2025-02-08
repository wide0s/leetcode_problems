from collections import OrderedDict

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        f = OrderedDict()
        for k in s:
            if k not in f:
                f[k] = [i, 1]
            else:
                f[k][1] += 1
        for k in f:
            if f[k][1] == 1:
                return f[k][0]
        return -1

vectors = [
        'leetcode', 0,
        'loveleetcode', 2,
        'aabb', -1
        ]

for i in range(0, len(vectors), 2):
    s = vectors[i]
    print(s)
    expected = vectors[i+1]
    returned = Solution().firstUniqChar(s)
    assert expected == returned, f'for \'{s}\' expected \'{expected}\', but returned \'{returned}\''
