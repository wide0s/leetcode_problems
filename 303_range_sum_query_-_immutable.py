class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.partial = [0]
        for i in range(0, len(nums)):
            self.partial.append(self.partial[i] + nums[i])

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.partial[right + 1] - self.partial[left]

vectors = [
    'NumArray', [-2, 0, 3, -5, 2, -1], None,
    'sumRange', [0, 2], 1,
    'sumRange', [2, 5], -1,
    'sumRange', [0, 5], -3,
    'NumArray', [-4,-5], None,
    'sumRange', [0, 0], -4,
    'sumRange', [1, 1], -5,
    'sumRange', [0, 1], -9,
    'sumRange', [1, 1], -5,
    'sumRange', [0, 0], -4
]

na = None
for i in range(0, len(vectors), 3):
    action = vectors[i]
    params = vectors[i + 1]
    expected = vectors[i + 2]
    returned = None
    print(f'action = {action}, params = {params}, expected = {expected}')
    if action == 'NumArray':
        na = NumArray(params)
    elif action == 'sumRange':
        returned = na.sumRange(params[0], params[1])
    assert expected == returned, f'expected {expected}, returned {returned}!'