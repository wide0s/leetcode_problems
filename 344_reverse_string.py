class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i, j = i + 1, j - 1

vectors = [
        [], [],
        ['h'], ['h'],
        ["h","e","l","l","o"], ["o","l","l","e","h"],
        ["H","a","n","n","a","h"], ["h","a","n","n","a","H"]
        ]

for i in range(0, len(vectors), 2):
    s = [ c for c in vectors[i] ]
    print(s)
    expected = vectors[i+1]
    Solution().reverseString(s)
    assert expected == s, f'for \'{vectors[i]}\' expected {expected}, but returned {s}'
