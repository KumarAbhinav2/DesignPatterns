class Singleton:
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class ParkingRate:
    def __init__(self, hr=1, rate=200):
        self.__hr = hr
        self.__rate = rate

    def getRate(self, rate):
        self.__rate = rate


class ParkingLot(metaclass=Singleton):

    def __init__(self, name, address):
        self.__name = name
        self.__address = address
        self.__rate = ParkingRate()

    def get_new_parking_ticket(self, vehicle):
        pass

    def is_full(self, type):
        pass

    def add_parking_floor(self):
        pass

    def add_entrance_kiosk(self):
        pass

    def add_exit_kiosk(self):
        pass







