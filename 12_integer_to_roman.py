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

vector = [
    3, 'III',
    4, 'IV',
    9, 'IX',
    58, 'LVIII',
    1994, 'MCMXCIV',
    3749, 'MMMDCCXLIX'
]

for i in range(0, len(vector), 2):
    number = vector[i]
    expected = vector[i + 1]
    print(f'{number} {expected}')
    returned = Solution().intToRoman(number)
    assert expected == returned, f'for number = {number} expected {expected}, returned {returned}!'
