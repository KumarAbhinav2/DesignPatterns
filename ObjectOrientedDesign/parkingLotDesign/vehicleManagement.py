from ObjectOrientedDesign.parkingLotDesign.contants import VehicleType as VT
from abc import ABC


class Vehicle(ABC):
    def __init__(self, license_number, type, ticket = None):
        self.__license_no = license_number
        self.__type = type
        self.__ticket_no = ticket

    def assign_ticket(self, ticket):
        self.__ticket_no = ticket


class Car(Vehicle):
    def __init__(self, license_number, ticket = None):
        super().__init__(license_number, VT.CAR, ticket)


class Bike(Vehicle):
    def __init__(self, license_number, ticket = None):
        super().__init__(license_number, VT.BIKE, ticket)


class TRUCK(Vehicle):
    def __init__(self, license_number, ticket = None):
        super().__init__(license_number, VT.TRUCK, ticket)