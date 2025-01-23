class Solution(object):
    cache = { 0: '1' }

    def rle(self, value):
        if not value:
            return '1'
        output = ''
        i = 0
        while i < len(value):
            j = i
            while j < len(value):
                if value[i] != value[j]:
                    break
                j += 1
            output += str(j - i) + value[i]
            i = j
        return output

    def countAndSayFast(self, n):
        """
        :type n: int
        :rtype: str
        """
        index = min(len(Solution.cache), n) - 1
        value = Solution.cache[index]
        for i in range(n - index - 1):
            value = self.rle(value)
            if index + i + 1 not in Solution.cache:
                Solution.cache[index + i + 1] = value
        return value

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        value = None
        for i in range(n):
            value = self.rle(value)
        return value

vectors = [ 1, '1', 2, '11', 3, '21', 4, '1211', 5, '111221', 6, '312211' ]
for i in range(0, len(vectors), 2):
    value = Solution().countAndSay(vectors[i])
    assert value == vectors[i + 1], f'SLOW: {vectors[i]} is {vectors[i + 1]}, but returned {value}'

for i in range(0, len(vectors), 2):
    value = Solution().countAndSayFast(vectors[i])
    assert value == vectors[i + 1], f'FAST: {vectors[i]} is {vectors[i + 1]}, but returned {value}'
