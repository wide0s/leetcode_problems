#You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
#The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
#Increment the large integer by one and return the resulting array of digits.

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for index in range(len(digits) - 1, -1, -1):
            if digits[index] + carry < 10:
                digits[index] += carry
                carry = 0
                break
            else:
                digits[index] += carry - 10 
                carry = 1
        if carry == 1:
            digits = [1] + digits
        return digits

vectors = [
        [0], [1],
        [1], [2],
        [3], [4],
        [4], [5],
        [5], [6],
        [6], [7],
        [7], [8],
        [8], [9],
        [9], [1,0],
        [1,9], [2,0],
        [9,9], [1,0,0]
        ]

for i in range(0, len(vectors), 2):
    digits = vectors[i]
    expected = vectors[i + 1]
    print(f'{digits} {expected}')
    returned = Solution().plusOne(digits)
    assert expected == returned, f'for {digits} expected {expected}, returned {returned}!'
