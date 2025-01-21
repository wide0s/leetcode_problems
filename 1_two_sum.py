class Solution1(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lst = sorted(nums)
        r = len(lst) - 1
        l = 0
        while l < r:
            #print(f"{lst[l]} {lst[r]}")
            if lst[l] + lst[r] < target:
                l += 1
            elif lst[l] + lst[r] > target:
                r -= 1
            else:
                break
            #print(f"l:{l} r:{r}")
        out = []
        for k, num in enumerate(nums):
            if num == lst[l] or num == lst[r]:
                out.append(k)
            if len(out) == 2:
                break
        return sorted(out)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff], i]
            else:
                seen[nums[i]] = i


print(Solution().twoSum([7, 2], 9))
print(Solution().twoSum([2, 7, 11, 15], 9))
print(Solution().twoSum([3, 2, 4], 6))
print(Solution().twoSum([3, 3], 6))
print(Solution().twoSum([2,5,5,11], 10))
print(Solution().twoSum([-10,-1,-18,-19], -19))
