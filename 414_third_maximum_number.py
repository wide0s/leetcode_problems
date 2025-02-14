# https://leetcode.com/problems/third-maximum-number/
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return max(nums)
        M = [nums[0]] # an array to store maximum
                      # values M[0] > M[1] > M[2]
        for n in nums:
            if n in M: # because we're looking for
                       #distinct numbers
                continue
            if n > M[0]:
                if len(M) == 3:
                    M[2] = M[1]
                    M[1] = M[0]
                elif len(M) == 2:
                    M.append(M[1])
                    M[1] = M[0]
                else:
                    M.append(M[0])
                M[0] = n
            elif len(M) > 1 and n > M[1]:
                if len(M) == 2:
                    M.append(M[1])
                else:
                    M[2] = M[1]
                M[1] = n
            elif len(M) == 1: # and M[0] >= n
                M.append(n)
            elif len(M) == 3 and n > M[2]:
                M[2] = n
            elif len(M) == 2: # and M[1] >= n
                M.append(n)
        return M[2] if len(M) == 3 and M[0] != M[1] != M[2] else max(M)

vectors = [
        [1,1,100], 100,
        [3,2,1], 1,
        [1,1,2], 2,
        [1,2], 2,
        [2,2,3,1], 1,

        ]

for i in range(0, len(vectors), 2):
    nums = vectors[i]
    print(nums)
    expected = vectors[i+1]
    returned = Solution().thirdMax(nums)
    assert expected == returned, f'for {nums} expected {expected}, but returned {returned}!'
