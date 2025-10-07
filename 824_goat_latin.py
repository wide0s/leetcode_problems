class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        output = suffix = word = ''
        for char in sentence + ' ':
            if char != ' ':
                word += char
                continue
            suffix += 'a'
            if suffix != 'a':
                output += ' '
            if word[0] in "aAeEiIoOuU":
                output += word + 'ma' + suffix
            else:
                output += word[1:] + word[0] + 'ma' + suffix
            word = ''
        return output

vectors = [
    ["I speak Goat Latin", "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"],
    ["The quick brown fox jumped over the lazy dog", "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"]
]

for vector in vectors:
    sentence = vector[0]
    expected = vector[1]
    print(f'for \'{sentence}\' expected \'{expected}\'')
    returned = Solution().toGoatLatin(sentence)
    assert expected == returned, f', but returned \'{returned}\'!'