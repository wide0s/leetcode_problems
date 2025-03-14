class ATM(object):

    def __init__(self):
        self.funds = [0] * 5
        self.banknotes = [20,50,100,200,500]


    def deposit(self, banknotesCount):
        """
        :type banknotesCount: List[int]
        :rtype: None
        """
        for i in range(len(self.funds)):
            self.funds[i] += banknotesCount[i]


    def withdraw(self, amount):
        """
        :type amount: int
        :rtype: List[int]
        """
        transaction = [0] * len(self.funds)
        for i in range(len(self.funds) - 1, -1, -1):
            q = min(amount // self.banknotes[i], self.funds[i])
            if self.funds[i] >= q:
                self.funds[i] -= q
                amount -= q * self.banknotes[i]
                transaction[i] = q
        if amount != 0:
            self.deposit(transaction)
            return [-1]
        return transaction


vectors = [
        'ATM', None, None,
        'deposit', [0,0,1,2,1], [0,0,1,2,1],
        'withdraw', 600, [0,0,1,0,1],
        'deposit', [0,1,0,1,1], [0,1,0,3,1],
        'withdraw', 600, [-1],
        'withdraw', 550, [0,1,0,0,1],
        'ATM', None, None,
        'deposit', [250796,638723,691758,845522,938973], [250796,638723,691758,845522,938973],
        'deposit', [215317,848628,182949,784609,30472], [466113,1487351,874707,1630131,969445],
        'withdraw', 701035245, [-1],
        'withdraw', 109992310, [-1],
        'withdraw', 755819795, [-1],
        'withdraw', 722349970, [1,1,0,1188137,969445]
        ]

atm = None
for i in range(0, len(vectors), 3):
    action = vectors[i]
    data = vectors[i + 1]
    expected = vectors[i + 2]
    print(f'{action}: data = {data}, expected = {expected}')
    if action == 'ATM':
        atm = ATM()
    elif action == 'deposit':
        atm.deposit(data)
        assert atm.funds == expected, f'expected funds are {expected}, but actual are {atm.funds}!'
    elif action == 'withdraw':
        returned = atm.withdraw(data)
        assert returned == expected, f'returned {returned}!'
