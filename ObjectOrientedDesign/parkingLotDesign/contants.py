from enum import Enum


class Slot(Enum):
    SINGLE = 1
    LMV = 2
    HMV = 3
    ELECTRIC = 4
    HANDICAPPED = 5


class VehicleType(Enum):
    BIKE = 1
    CAR = 2
    TRUCK = 3


class AccountStatus(Enum):
    ACTIVE = 1
    INACTIVE = 2
    SUSPENDED = 3


class TicketStatus(Enum):
    ACTIVE = 1
    PAID = 2
    LOST = 3




