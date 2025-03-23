#Today I learned that every palindromic number with an even number of digits is a multiple of 11.
#Every number (in decimal) that is a palindrome and has an even number of digits is divisible by 11.

#The condition is not true the other way around however; a number times 11 will not nessecarily be 
#an even-digit palindrome. But every palindrome with an even number of digits is a multiple of 11.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        a = []
        while x > 0:
            r = x % 10
            x = x // 10
            a.append(r)
        l = 0
        r = len(a) - 1
        while l < r:
            if a[l] != a[r]:
                return False
            l += 1
            r -= 1
        return True

vectors = [
    -12321, False,
    1, True,
    12321, True,
    12345654321, True,
    1441, True
]

for i in range(0, len(vectors), 2):
    x = vectors[i]
    expected = vectors[i + 1]
    print(f'{x} {expected}')
    returned = Solution().isPalindrome(x)
    assert expected == returned, f'for x = {x} expected {expected}, returned {returned}!'
