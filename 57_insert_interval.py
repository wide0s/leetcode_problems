class Solution(object):
    # Runtime complexity: O(n*log(n))
    # Space complexity: O(2*n)
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        # it can be optimized without using sorting
        ins = sorted([newInterval] + intervals, key = lambda x : x[0])
        stack = [ins[0]]
        for curr in ins:
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
        [], [0,1], [[0,1]],
        [[1,3], [6,9]], [-1,0], [[-1,0], [1,3], [6,9]],
        [[1,3], [6,9]], [2,5], [[1,5], [6,9]],
        [[1,2], [3,5], [6,7], [8,10], [12,16]], [4,8], [[1,2],[3,10],[12,16]],
        [[1,5]], [6,8], [[1,5], [6,8]],
        [[1,5]], [0,3], [[0,5]],
        [[2,3], [5,7]], [0,6], [[0,7]]
        ]

for i in range(0, len(vectors), 3):
    intervals = vectors[i]
    newInterval = vectors[i + 1]
    print(f'{intervals}, {newInterval}')
    expected = vectors[i + 2]
    returned = Solution().insert(intervals, newInterval)
    assert expected == returned, f'for {intervals} and {newInterval} expected {expected}, but returned {returned}!'
