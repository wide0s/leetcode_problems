class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []

        D2L = [[''],
               [''],
               ['a','b','c'],
               ['d','e','f'],
               ['g','h','i'],
               ['j','k','l'],
               ['m','n','o'],
               ['p','q','r','s'],
               ['t','u','v'],
               ['w','x','y','z']]

        a = ['']
        for d in digits:
            combinations = []
            for c1 in a:
                for c2 in D2L[int(d)]:
                    combinations.append(c1 + c2)
            a = combinations
        return a

vectors = [
        "", [],
        "0", [""],
        "1", [""],
        "2", ["a", "b", "c"],
        "23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"],
        "234", ['adg', 'adh', 'adi', 'aeg', 'aeh', 'aei', 'afg', \
                'afh', 'afi', 'bdg', 'bdh', 'bdi', 'beg', 'beh', \
                'bei', 'bfg', 'bfh', 'bfi', 'cdg', 'cdh', 'cdi', \
                'ceg', 'ceh', 'cei', 'cfg', 'cfh', 'cfi'],
        "2349", ['adgw', 'adgx', 'adgy', 'adgz', 'adhw', 'adhx', \
                 'adhy', 'adhz', 'adiw', 'adix', 'adiy', 'adiz', \
                 'aegw', 'aegx', 'aegy', 'aegz', 'aehw', 'aehx', \
                 'aehy', 'aehz', 'aeiw', 'aeix', 'aeiy', 'aeiz', \
                 'afgw', 'afgx', 'afgy', 'afgz', 'afhw', 'afhx', \
                 'afhy', 'afhz', 'afiw', 'afix', 'afiy', 'afiz', \
                 'bdgw', 'bdgx', 'bdgy', 'bdgz', 'bdhw', 'bdhx', \
                 'bdhy', 'bdhz', 'bdiw', 'bdix', 'bdiy', 'bdiz', \
                 'begw', 'begx', 'begy', 'begz', 'behw', 'behx', \
                 'behy', 'behz', 'beiw', 'beix', 'beiy', 'beiz', \
                 'bfgw', 'bfgx', 'bfgy', 'bfgz', 'bfhw', 'bfhx', \
                 'bfhy', 'bfhz', 'bfiw', 'bfix', 'bfiy', 'bfiz', \
                 'cdgw', 'cdgx', 'cdgy', 'cdgz', 'cdhw', 'cdhx', \
                 'cdhy', 'cdhz', 'cdiw', 'cdix', 'cdiy', 'cdiz', \
                 'cegw', 'cegx', 'cegy', 'cegz', 'cehw', 'cehx', \
                 'cehy', 'cehz', 'ceiw', 'ceix', 'ceiy', 'ceiz', \
                 'cfgw', 'cfgx', 'cfgy', 'cfgz', 'cfhw', 'cfhx', \
                 'cfhy', 'cfhz', 'cfiw', 'cfix', 'cfiy', 'cfiz']
        ]

for i in range(0, len(vectors), 2):
    digits = vectors[i]
    print(digits)
    expected = vectors[i+1]
    returned = Solution().letterCombinations(digits)
    assert expected == returned, f'for \'{digits}\' expected {expected}, but returned {returned}!'
