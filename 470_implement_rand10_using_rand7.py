# ref https://algo.monster/liteproblems/470
from random import randint

def rand7():
    return randint(1, 7)

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        r = 41
        while r > 40:
            r = 7 * (rand7() - 1) + rand7() # 1, 2, ..., 49
        return (r % 10) + 1

for i in range(1, 10):
    r = Solution().rand10()
    print(f'Unif(1,10) sample {r}')
