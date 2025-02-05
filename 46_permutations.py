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

# Ehrlich algorithm https://yandex.ru/video/touch/preview/17770729873463663004
# Heap algorithm https://youtu.be/-HAJoD_6PQA?si=Jaa4RPcRc0d2Ioh9

class Solution(object):
    def permute2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Heap's algorithm
        def heap_permutation(a, k, copy_on_return=True):
            if k == 1:
                yield list(a) if copy_on_return else a
            else:
                for i in range(k):
                    for hp in heap_permutation(a, k - 1, copy_on_return):
                        yield hp
                    index = (k % 2) * i
                    a[index], a[k - 1] = a[k - 1], a[index]

        return [ p for p in heap_permutation(nums, len(nums)) ]

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Ehrlich's algorithm
        def ehrlich_permutation(o, copy_on_return=True):
            n = len(o)
            a = list(o)
            b = [ i for i in range(0, n) ]
            c = [ 0 for _ in range(0, n + 1) ]
            while True:
                # new permutation
                yield list(a) if copy_on_return else a
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
 
        return [ p for p in ehrlich_permutation(nums) ]

vectors = [
        [1,2,3,4], [[1,2,3,4],[2,1,3,4],[3,1,2,4],[1,3,2,4],[2,3,1,4],[3,2,1,4],[4,2,1,3],[1,2,4,3],[2,1,4,3],[4,1,2,3],[1,4,2,3],[2,4,1,3],[3,4,1,2],[4,3,1,2],[1,3,4,2],[3,1,4,2],[4,1,3,2],[1,4,3,2],[2,4,3,1],[3,4,2,1],[4,3,2,1],[2,3,4,1],[3,2,4,1],[4,2,3,1]],
        [1,2,3], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]],
        [1,1,2], [[1,1,2],[1,1,2],[2,1,1],[1,2,1],[1,2,1],[2,1,1]],
        [0,1], [[0,1],[1,0]],
        [1], [[1]]
        ]

for i in range(0, len(vectors), 2):
    sequence = vectors[i]
    print(sequence)
    expected = sorted(vectors[i+1])
    returned = Solution().permute(sequence)
    assert expected == sorted(returned), f'ehrlich: for sequence {sequence} expected {expected}, but returned {returned}!'
    returned = Solution().permute2(sequence)
    assert expected == sorted(returned), f'heap: for sequence {sequence} expected {expected}, but returned {returned}!'
