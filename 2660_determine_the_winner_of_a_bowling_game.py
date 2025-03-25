class Solution(object):
    def isWinner(self, player1, player2):
        """
        :type player1: List[int]
        :type player2: List[int]
        :rtype: int
        """
        players = [player1, player2]
        strikes = [0, 0]
        scores = [0, 0]
        for i in range(len(player1)):
            for j in range(len(players)):
                p = players[j]
                if strikes[j] != 0:
                    scores[j] += 2 * p[i]
                    strikes[j] -= 1
                else:
                    scores[j] += p[i]
                if p[i] == 10:
                    strikes[j] = 2
        return 1 if scores[0] > scores[1] else 2 if scores[0] < scores[1] else 0

vectors = [
    [[5,10,3,2], [6,5,7,3]], 1,
    [[3,5,7,6], [8,10,10,2]], 2,
    [[2,3], [4,1]], 0,
    [[1,1,1,10,10,10,10], [10,10,10,10,1,1,1]], 2,
    [[7,7,4,7,7], [7,2,3,10,10]], 2
]

for i in range(0, len(vectors), 2):
    players = vectors[i]
    expected = vectors[i + 1]
    print(f'{players} {expected}')
    returned = Solution().isWinner(*players)
    assert expected == returned, f'for {players} expected {expected}, returned {returned}!'