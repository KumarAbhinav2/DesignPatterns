from enum import Enum
class BookFormat(Enum):
    HARDCOVER = 1
    PAPERBACK = 2
    EBOOK = 3
    KINDLE = 4
    MAGAZINE = 5
    JOURNAL = 6

class BookStatus(Enum):
    AVAILABLE = 1
    LOANED = 2
    RESERVED = 3
    LOST = 4

class AccountStatus(Enum):
    ACTIVE = 1
    SUSPENDED = 2
    CLOSED = 3
    CANCELLED = 4

class Address:
    def __init__(self, addressline1, city, state, pin, country, addressline2=None):
        self.addressline1 = addressline1
        self.addressline2 = addressline2
        self.city = city
        self.state = state
        self.pin = pin
        self.country = country

class Constants:
    def __init__(self):
        self.MAX_BOOK_ISSUES_TO_USER = 5
        self.MAX_DAYS_ALLOWED = 10







