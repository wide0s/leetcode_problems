# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# II            2
# III           3
# IV            4
# V             5
# VI            6
# VII           7
# VIII          8
# IX            9
# X            10
# XI           11
# XII          12
# XIII         13
# XIV          14
# XV           15
# XVI          16
# XVII         17
# XVIII        18
# XIX          19
# XX           20


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

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = { 'I' : 1,
              'IV': 4,
              'V' : 5,
              'IX': 9,
              'X' : 10,
              'XL': 40,
              'L' : 50,
              'XC': 90,
              'C' : 100,
              'CD': 400,
              'D' : 500,
              'CM': 900,
              'M': 1000 }
        d = 0
        p = None
        for ch in s:
            if p is not None:
                if p + ch in m:
                    d += m[p + ch]
                    p = None
                else:
                    d += m[p]
                    p = ch
            else:
                p = ch
        if p is not None:
            d += m[p]
        return d


for d in range(1, 4000):
    roman = Solution().intToRoman(d)
    arabic = Solution().romanToInt(roman)
    assert d == arabic
