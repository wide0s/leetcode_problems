class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        n = 0
        for op in logs:
            if op == '../':
                n -= n > 0
            elif op == './':
                pass
            else:
                n += 1
        return n

vectors = [
    ["d1/","d2/","../","d21/","./"], 2,
    ["d1/","d2/","./","d3/","../","d31/"], 3,
    ["d1/","../","../","../"], 0,
]

for i in range(0, len(vectors), 2):
    logs = vectors[i]
    expected = vectors[i + 1]
    print(f'{logs} {expected}')
    returned = Solution().minOperations(logs)
    assert expected == returned, f'for {logs} expected {expected}, returned {returned}!'
