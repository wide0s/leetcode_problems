class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        i, j = 0, len(height) - 1
        while i < j:
            # runs faster than area = max(area, ...)
            curr = min(height[i], height[j]) * (j - i)
            if area < curr:
                area = curr
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return area
        
vectors = [
    [[1,8,6,2,5,4,8,3,7], 49],
    [[1,1],1]
]

for vector in vectors:
    params = vector[0]
    expected = vector[1]
    print(f'for {params} expected {expected}')
    returned = Solution().maxArea(params)
    assert expected == returned, f'for \'{params}\' expected {expected}, but returned {returned}!'