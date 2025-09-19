from collections import defaultdict
import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.grouped = defaultdict(list)
        for index, value in enumerate(nums):
            self.grouped[value].append(index)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        return random.choice(self.grouped[target])

vectors = [
    ['ctor', [1, 2, 3, 3, 3]],
    ['pick', 3],
    ['pick', 1],
    ['pick', 3],
]

returned = instance = None
for vector in vectors:
    action = vector[0]
    params = vector[1]
    if action == 'ctor':
        instance = Solution(params)
        returned = instance
    elif action == 'pick':
        returned = instance.pick(params)
    print(f'action = {action}, params = {params}, returned = {returned}')