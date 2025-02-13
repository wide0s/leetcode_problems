class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.spaces = [big, medium, small]

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        index = carType - 1
        if  0 <= index < len(self.spaces) and self.spaces[index] > 0:
            self.spaces[index] -= 1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
