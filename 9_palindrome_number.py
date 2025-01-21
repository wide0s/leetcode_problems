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

print(Solution().isPalindrome(-12321))
print(Solution().isPalindrome(1))
print(Solution().isPalindrome(12321))
print(Solution().isPalindrome(12345654321))
print(Solution().isPalindrome(1441))
