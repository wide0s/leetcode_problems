class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1 = version1.split('.')
        version2 = version2.split('.')
        for i in range(0, max(len(version1), len(version2))):
            d1 = int(version1[i]) if i < len(version1) else 0
            d2 = int(version2[i]) if i < len(version2) else 0
            if d1 > d2:
                return 1
            if d1 < d2:
                return -1
        return 0

vectors = [
        ['1.2', '1.10'], -1,
        ['1.01', '1.001'], 0,
        ['1.0', '1.0.0.0'], 0
        ]

for i in range(0, len(vectors), 2):
    params = vectors[i]
    expected = vectors[i + 1]
    print(f'{params} {expected}')
    returned = Solution().compareVersion(*params)
    assert expected == returned, f'for {params} expected {expected}, returned {returned}!'
