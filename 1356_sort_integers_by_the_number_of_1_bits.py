# You are given an integer array arr. Sort the integers
# in the array in ascending order by the number of 1's
# in their binary representation and in case of two or 
# more integers have the same number of 1's you have to
# sort them in ascending order.
#
# Return the array after sorting it.
#
# Constraints:
#  1 <= arr.length <= 500
#  0 <= arr[i] <= 104

class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        def popcount(d):
            # 32-bit recursive reduction using SWAR...
            # but first step is mapping 2-bit values
            # into sum of 2 1-bit values in sneaky way
            n = d
            n = n - ((n >> 1) & 0x55555555)
            n = (((n >> 2) & 0x33333333) + (n & 0x33333333))
            n = (((n >> 4) + n) & 0x0f0f0f0f)
            n += (n >> 8) + (n >> 16)
            return (n & 0x0000003f, d) # this is a trick to sort
                                       # by number of bits and by
                                       # value at the same time

        #def popcount_slow(d):
        #    n = d
        #    count = n & 0x1
        #    n >>= 1
        #    while n > 0:
        #        count += n & 0x1
        #        n >>= 1
        #    return (count, d)

        return sorted(arr, key=popcount)

vectors = [
        [0,1,2,3,4,5,6,7,8], [0,1,2,4,8,3,5,6,7],
        [1024,512,256,128,64,32,16,8,4,2,1], [1,2,4,8,16,32,64,128,256,512,1024],
        [9,8,7,1024,6,2], [2, 8, 1024, 6, 9, 7]
        ]

for i in range(0, len(vectors), 2):
    arr = [ x for x in vectors[i] ]
    print(arr)
    expected = vectors[i+1]
    returned = Solution().sortByBits(arr)
    assert expected == returned, f'for {arr} expected {expected}, but returned {returned}!'
