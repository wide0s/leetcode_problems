class Bitset(object):

    def __init__(self, size):
        """
        :type size: int
        """
        self.nb = 0
        self.bs = [0] * size
        self.flipped = False


    def fix(self, idx):
        """
        :type idx: int
        :rtype: None
        """
        if self.flipped:
            if self.bs[idx] == 1:
                self.nb += 1
            self.bs[idx] = 0
        else:
            if self.bs[idx] == 0:
                self.nb += 1
            self.bs[idx] = 1
        

    def unfix(self, idx):
        """
        :type idx: int
        :rtype: None
        """
        if self.flipped:
            if self.bs[idx] == 0:
                self.nb -= 1
            self.bs[idx] = 1
        else:
            if self.bs[idx] == 1:
                self.nb -= 1
            self.bs[idx] = 0


    def flip(self):
        """
        :rtype: None
        """
        self.flipped = not self.flipped
        self.nb = len(self.bs) - self.nb


    def all(self):
        """
        :rtype: bool
        """
        return len(self.bs) == self.count()


    def one(self):
        """
        :rtype: bool
        """
        return self.count() > 0


    def count(self):
        """
        :rtype: int
        """
        return self.nb
        

    def toString(self):
        """
        :rtype: str
        """
        return ''.join(str(1 - bit) for bit in self.bs) \
            if self.flipped else ''.join(str(bit) for bit in self.bs)


vectors = [
        'Bitset', 5, '00000',
        'fix', 3, '00010',
        'fix', 1, '01010',
        'flip', None, '10101',
        'all', None, False,
        'unfix', 0, '00101',
        'flip', None, '11010',
        'one', None, True,
        'unfix', 0, '01010',
        'count', None, 2,
        'toString', None, '01010',
        'Bitset', 2, '00',
        'flip', None, '11',
        'unfix', 1, '10',
        'all', None, False,
        'fix', 1, '11',
        'fix', 1, '11',
        'unfix', 1, '10',
        'all', None, False,
        'count', None, 1,
        'toString', None, '10',
        'toString', None, '10',
        'toString', None, '10',
        'unfix', 0, '00',
        'flip', None, '11',
        'all', None, True,
        'unfix', 0, '01',
        'one', None, True,
        'one', None, True,
        'all', None, False,
        'fix', 0, '11',
        'unfix', 0, '01',
        'Bitset', 256, ''.join(str(x) for x in [0] * 256),
        'flip', 0, ''.join(str(x) for x in [1] * 256),
        'unfix', 64, ''.join(str(x) for x in [1] * 64) + '0' + ''.join(str(x) for x in [1] * (256 - 65))
        ]

bs = None
for i in range(0, len(vectors), 3):
    action = vectors[i]
    value = vectors[i + 1]
    expected = vectors[i + 2]
    print(f'action = {action}, value = {value}, expected = {expected}')
    if action == 'Bitset':
        bs = Bitset(value)
        bs.toStringCalls = len(vectors)
        returned = bs.toString()
    elif action == 'fix':
        bs.fix(value)
        returned = bs.toString()
    elif action == 'unfix':
        bs.unfix(value)
        returned = bs.toString()
    elif action == 'flip':
        bs.flip()
        returned = bs.toString()
    elif action == 'one':
        returned = bs.one()
    elif action == 'all':
        returned = bs.all()
    elif action == 'count':
        returned = bs.count()
    elif action == 'toString':
        returned = bs.toString()
    assert returned == expected, f' returned {returned}!'
