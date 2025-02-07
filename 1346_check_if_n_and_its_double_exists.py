class Solution(object):
    # runtime beats 60%, O(n*log(n))
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        def bisection(a, target, left = 0):
            right = len(a)
            while left < right:
                mid = (right + left) // 2
                if a[mid] < target:
                    left = mid + 1
                elif a[mid] > target:
                    right = mid
                else:
                    return mid
            return -1
        arr = sorted(arr)
        for i in range(len(arr)):
            j = bisection(arr, 2 * arr[i])
            if j > -1 and i != j:
                return True
        return False

vectors = [
        [10,2,5,3], True,
        [3,1,7,11], False,
        [-10,12,-20,-8,15], True,
        [-2,0,10,-19,4,6,-8], False
        ]
for i in range(0, len(vectors), 2):
    arr = vectors[i]
    print(arr)
    expected = vectors[i+1]
    returned = Solution().checkIfExist(arr)
    assert expected == returned, f'for {arr} expected {expected}, but returned {returned}!'
