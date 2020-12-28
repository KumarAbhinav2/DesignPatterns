from ObjectOrientedDesign.parkingLotDesign.contants import AccountStatus as AS


class Account:

    def __init__(self, username, password, status = AS.ACTIVE):
        self.__username = username
        self.__password = password
        self.status = status

    def reset_password(self):
        pass


class ParkingAttendantPortal(Account):
    def __init__(self, username, password, status=AS.ACTIVE):
        super().__init__(username, password, status)

    def process_ticket(self, ticket_number):
        pass


class AdminPortal(Account):
    def __init__(self, username, password, status=AS.ACTIVE):
        super().__init__(username, password, status)

    def add_floor(self, floor):
        pass

    def add_entrance_kiosk(self, entrance_kiosk):
        pass

    def add_exit_kiosk(self, exit_kiosk):
        pass

    def add_parking_slot(self, slot):
        pass

    def add_display_board(self, floor, board):
        pass
