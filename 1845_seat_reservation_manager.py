from sortedcontainers import SortedSet

class SeatManager(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.seats = SortedSet([seat + 1 for seat in range(n)])

    def reserve(self):
        """
        :rtype: int
        """
        if len(self.seats) == 0:
            return 0 # seats are numbered starting from 1
        return self.seats.pop(0)


    def unreserve(self, seatNumber):
        """
        :type seatNumber: int
        :rtype: None
        """
        self.seats.add(seatNumber)

vectors = [
        "SeatManager", 6,
        "reserve", 1,
        "reserve", 2,
        "reserve", 3,
        "reserve", 4,
        "unreserve", 1,
        "unreserve", 2,
        "reserve", 1,
        "reserve", 2,
        "reserve", 5,
        "unreserve", 4,
        "reserve", 4,
        "reserve", 6
        ]

sm = None
for i in range(0, len(vectors), 2):
    action = vectors[i]
    data = vectors[i + 1]
    print(f'action={action}, data={data}')
    if action == "SeatManager":
        sm = SeatManager(data)
    elif action == "reserve":
        returned = sm.reserve()
        assert returned == data, f'for {action}() call expected {data}, returned {returned}!'
    elif action == "unreserve":
        sm.unreserve(data)
