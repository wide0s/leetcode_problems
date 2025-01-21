class Solution(object):
    def intToRoman(self, number):
        num = [1,    4,    5,   9,   10,   40,  50,  90,  100,  400,  500, 900, 1000]
        sym = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
        i = 12
        roman = ''
        while number:
            div = number // num[i]
            number %= num[i]
            while div:
                roman += sym[i]
                div -= 1
            i -= 1
        return roman

assert Solution().intToRoman(3749) == 'MMMDCCXLIX'
assert Solution().intToRoman(58) == 'LVIII'
assert Solution().intToRoman(1994) == 'MCMXCIV'
