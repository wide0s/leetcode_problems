# Given an array nums of distinct integers, return
# all the possible permutations. You can return the
# answer in any order.
#
# Example 1:
#  Input: nums = [1,2,3]
#  Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:
#  Input: nums = [0,1]
#  Output: [[0,1],[1,0]]
# Example 3:
#  Input: nums = [1]
#  Output: [[1]]

# lesson https://yandex.ru/video/touch/preview/17770729873463663004

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Ehrlich's algorithm
        def next_permutation(o, copy_on_return=True):
            n = len(o)
            a = list(o)
            b = [ i for i in range(0, n) ]
            c = [ 0 for _ in range(0, n + 1) ]
            p = None
            while True:
                # 159ms, Beats 24.69%
                if p != a:
                    p = list(a) if copy_on_return else a
                    yield p
                k = 1
                while c[k] == k:
                    c[k] = 0
                    k += 1
                # reached the end, terminating
                if k == n:
                    return
                c[k] += 1
                # swap a[0] <-> a[b[k]]
                a[0], a[b[k]] = a[b[k]], a[0]
                j = 1
                k -= 1
                # flip the list j in [1, k - 1)
                while j < k:
                    b[j], b[k] = b[k], b[j]
                    j += 1
                    k -= 1
        p = []
        for x in sorted(next_permutation(nums)):
            if len(p) == 0:
                p += [x]
            elif p[-1] != x:
                p += [x]
        return p

vectors = [
        [1,2,3], [[1,2,3],[2,3,1],[1,3,2],[3,1,2],[2,1,3],[3,2,1]],
        [1,1,2], [[1,1,2],[2,1,1],[1,2,1]],
        [1], [[1]]
        ]

for i in range(0, len(vectors), 2):
    sequence = vectors[i]
    print(sequence)
    expected = vectors[i+1]
    returned = Solution().permute(sequence)
    print(returned)
    assert sorted(expected) == sorted(returned), f'for sequence {sequence} expected {expected}, but returned {returned}!' 
