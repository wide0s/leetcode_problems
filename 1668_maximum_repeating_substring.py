# For a string sequence, a string word is k-repeating if word
# concatenated k times is a substring of sequence. The word's
# maximum k-repeating value is the highest value k where word
# is k-repeating in sequence. If word is not a substring of
# sequence, word's maximum k-repeating value is 0.
#
# Given strings sequence and word, return the maximum k-repeating
# value of word in sequence.
#
# Constraints:
#  (*) 1 <= sequence.length <= 100
#  (*) 1 <= word.length <= 100
#  (*) sequence and word contains only lowercase English letters.

class Solution(object):
    # runtime beats 100%, memory beats 64%
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        repetitions = matches = index = 0
        while index < len(sequence):
            if sequence[index:index + len(word)] == word:
                matches += 1
                repetitions = max(repetitions, matches)
                index += len(word)
            else:
                if matches > 0:
                    # step back one fragment and restart
                    # the search to handle case like:
                    # aaabaaabaaaabaaaaba word=aaaba
                    index -= len(word)
                index += 1
                matches = 0
        return repetitions

vectors = [
        "ababc", "ab", 2,
        "ababc", "ba", 1,
        "ababc", "ac", 0,
        "zabzababzabababzabababab", "ab", 4,
        "zababababzabab", "ab", 4,
        "ab", "ab", 1,
        "aaabaaaabaaabaaaabaaaabaaaabaaaaba", "aaaba", 5
        ]

for i in range(0, len(vectors), 3):
    sequence = vectors[i]
    word = vectors[i+1]
    expected = vectors[i+2]
    print(f'sequence {sequence} word {word} expected {expected}')
    returned = Solution().maxRepeating(sequence, word)
    assert expected == returned, f'for sequence \'{sequence}\' and word \'{word}\' expected {expected}, but returned {returned}!' 
