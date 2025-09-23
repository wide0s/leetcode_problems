# ref https://leetcode.com/problems/design-movie-rental-system/solutions/7210724/design-movie-rental-system-complete-mult-k2ix/
from sortedcontainers import SortedList
from collections import defaultdict

class MovieRentingSystem(object):

    def __init__(self, n, entries):
        """
        :type n: int
        :type entries: List[List[int]]
        """
        self.unrented = defaultdict(lambda: SortedList()) # [movie] = SortedList((price, shop), ...)
        self.rented = SortedList() # list of (price, shop, movie)
        self.prices = {} # [(shop, movie)] = price

        for shop, movie, price in entries:
            self.unrented[movie].add((price, shop)) # sorted by price and shop
            self.prices[(shop, movie)] = price

    def search(self, movie):
        """
        :type movie: int
        :rtype: List[int]
        """
        if movie not in self.unrented:
            return []
        sorted_list = self.unrented[movie] # sorted list of (price, shop), ...
        return [shop for _, shop in sorted_list[:5]]


    def rent(self, shop, movie):
        """
        :type shop: int
        :type movie: int
        :rtype: None
        """
        price = self.prices[(shop, movie)]
        self.unrented[movie].remove((price, shop))
        self.rented.add((price, shop, movie)) # sorted by price, shop and movie

    def drop(self, shop, movie):
        """
        :type shop: int
        :type movie: int
        :rtype: None
        """
        price = self.prices[(shop, movie)]
        self.rented.remove((price, shop, movie))
        self.unrented[movie].add((price, shop))

    def report(self):
        """
        :rtype: List[List[int]]
        """
        return [[shop, movie] for _, shop, movie in self.rented[:5]]


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()

vectors = [
    ['ctor', [3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]]], None],
    ['search', [1], [1, 0, 2]],
    ['rent', [0, 1], None],
    ['rent', [1, 2], None],
    ['report', [], [[0, 1], [1, 2]]],
    ['drop', [1, 2], None],
    ['search', [2], [0, 1]]
]

instance = None
for vector in vectors:
    action = vector[0]
    params = vector[1]
    expected = vector[2]
    returned = None
    print(f'action \'{action}\' and params {params} expected {expected}')
    if action == 'ctor':
        instance = MovieRentingSystem(*params)
    elif action == 'search':
        returned = instance.search(*params)
    elif action == 'rent':
        returned = instance.rent(*params)
    elif action == 'report':
        returned = instance.report(*params)
    elif action == 'drop':
        returned = instance.drop(*params)
    else:
        raise Exception('unsupported action!')
    assert returned == expected, f'for action \'{action}\' and params {params} expected {expected}, but returned {returned}!'