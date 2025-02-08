class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = [''] * len(s)
        vowels = set('aeiouAEIOUA')
        i, j = 0, len(s) - 1
        while i <= j:
            if s[i] not in vowels:
                a[i] = s[i]
                i += 1
                continue
            if s[j] not in vowels:
                a[j] = s[j]
                j -= 1
                continue
            a[i], a[j] = s[j], s[i]
            i, j = i + 1, j - 1
        return ''.join(a)

vectors = [
        '', '',
        'IceCreAm', 'AceCreIm',
        'leetcode', 'leotcede',
        'InGeniCO', 'OnGineCI',
        'zEna', 'zanE',
        'Hola!', 'Halo!',
        'Mir', 'Mir'
        ]

for i in range(0, len(vectors), 2):
    s = vectors[i]
    print(s)
    expected = vectors[i+1]
    returned = Solution().reverseVowels(s)
    assert expected == returned, f'for \'{s}\' expected \'{expected}\', but returned \'{returned}\''
