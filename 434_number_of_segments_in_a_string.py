class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())

vectors = [
        " The   quick  brown  fox  jumps  over  the lazy   dog ", 9, 
        "Hello, my name is John", 5,
        "Hello", 1,
        "", 0
        ]

for i in range(0, len(vectors), 2):
    s = vectors[i]
    expected = vectors[i + 1]
    print(f'\'{s}\' {expected}')
    returned = Solution().countSegments(s)
    assert expected == returned, f'for {s} expected {expected}, returned {returned}!'
