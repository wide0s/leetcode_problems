class Solution(object):
    def numberOfLines(self, widths, s):
        """
        :type widths: List[int]
        :type s: str
        :rtype: List[int]
        """
        output = [1, 0]
        for c in s:
            idx = ord(c) - ord('a')
            if output[1] + widths[idx] > 100:
                output[1] = 0
                output[0] += 1
            output[1] += widths[idx]
        return output

vectors = [
        [1,98,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], "a", [1,1],
        [1,98,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], "abcccccccccccccccccccccccc", [1,99],
        [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], "abcdefghijklmnopqrstuvwxyz", [3,60],
        [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], "bbbcccdddaaa", [2,4]
        ]

for i in range(0, len(vectors), 3):
    widths = vectors[i]
    s = vectors[i + 1]
    print(f'{widths} \'{s}\'')
    expected = vectors[i + 2]
    returned = Solution().numberOfLines(widths, s)
    assert expected == returned, f'for {widths} and {s} expected {expected}, but returned {returned}!'
