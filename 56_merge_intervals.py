class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0:
            return []
        ins = sorted(intervals, key=lambda x: x[0])
        stack = [ins[0]]
        for curr in ins[1:]:
            if curr[0] > stack[-1][1]:
                # intervals do not overlap
                stack.append(curr)
            else:
                # intervals overlap, so we merge them into one
                prev = stack.pop()
                union = [min(prev[0], curr[0]), max(prev[1], curr[1])]
                stack.append(union)
        return stack

vectors = [
        [[1,3], [2,6], [8,10],[15,18]], [[1,6], [8,10], [15,18]],
        [[1,4], [4,5]], [[1,5]]
        ]

for i in range(0, len(vectors), 2):
    intervals = vectors[i]
    print(intervals)
    expected = vectors[i + 1]
    returned = Solution().merge(intervals)
    assert expected == returned, f'for {intervals} expected {expected}, but returned {returned}!'
