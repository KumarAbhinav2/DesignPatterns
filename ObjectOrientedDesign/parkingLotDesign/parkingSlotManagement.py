from ObjectOrientedDesign.parkingLotDesign.contants import Slot


class ParkingSlot:
    def __init__(self, type, number):
        self.__number = number
        self.__type = type
        self.__isfree = True
        self.__vehicle = None

    def is_free(self):
        return self.__isfree

    def assign_vehicle(self, vehicle):
        self.__vehicle = vehicle
        self.__isfree = False

    def remove_vehicle(self):
        self.__vehicle = None
        self.__isfree = True


class Single(ParkingSlot):
    def __init__(self, number):
        super().__init__(Slot.SINGLE, number)


class LMV(ParkingSlot):
    def __init__(self, number):
        super().__init__(Slot.LMV, number)


class HMV(ParkingSlot):
    def __init__(self, number):
        super().__init__(Slot.HMV, number)


class Handicapped(ParkingSlot):
    def __init__(self, number):
        super().__init__(Slot.HANDICAPPED, number)


class Electric(ParkingSlot):
    def __init__(self, number):
        super().__init__(Slot.ELECTRIC, number)

