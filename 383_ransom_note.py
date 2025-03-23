from collections import defaultdict

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(magazine) < len(ransomNote):
            return False
        freqs = defaultdict(int)
        for c in magazine:
            freqs[c] += 1
        for c in ransomNote:
            freqs[c] -= 1
            if freqs[c] < 0:
                return False
        return True

vectors = [
    'a', 'b', False,
    'aa', 'ab', False,
    'aa', 'aab', True,
    'aabbbcddddeeeeexzxyz', 'aabbcddddeeeeexxzzwwwwww', False
]

for i in range(0, len(vectors), 3):
    ransomNote = vectors[i]
    magazine = vectors[i + 1]
    expected = vectors[i + 2]
    print(f'ransomeNote {ransomNote} magazine {magazine}')
    returned = Solution().canConstruct(ransomNote, magazine)
    assert expected == returned, f'for ransom note \'{ransomNote}\' and magazine \'{magazine}\' exected {expected}, returned {returned}!'

