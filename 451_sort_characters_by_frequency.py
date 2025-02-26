from collections import defaultdict

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None:
            return None
        freqs = defaultdict(int)
        for c in s:
            freqs[c] += 1
        freqs = sorted(freqs.items(), key = lambda item: item[1], reverse = True)
        return ''.join([ e[0] * e[1] for e in freqs ])

vectors = [
        None, None,
        "", "",
        "cCCbbbbbefefjjjjaaaa", "bbbbbjjjjaaaaCCeeffc",
        "tree", "eetr",
        "cccaaa", "cccaaa",
        "Aabb", "bbAa"
        ]

for i in range(0, len(vectors), 2):
    s = vectors[i]
    expected = vectors[i + 1]
    print(f'{expected} is a frequency sorted {s}')
    returned = Solution().frequencySort(s)
    assert expected == returned, f'for {s} expected {expected}, but returned {returned}!'
