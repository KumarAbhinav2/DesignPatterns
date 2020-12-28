from ObjectOrientedDesign.parkingLotDesign.contants import Slot
import uuid


class DisplayBoard:
    def __init__(self, id):
        self.id = id
        self.free_slots = {}

    def show_empty_slot(self):
        for slot in self.free_slots:
            if slot.is_free():
                print(f"Free Slot Available for {slot.name}: {slot.get_number()}")


class ParkingFloor:
    def __init__(self, name):
        self.name = name
        self.spots = {}
        self.displayBoard = DisplayBoard(uuid.uuid1())

    def add_parking_slot(self, slot):
        self.spots.get(slot.get_slot_type(), "Wrong parking slot selected")

    def assign_vehicle(self, vehicle, slot):
        slot.assign_vehicle(vehicle)
        self.update_slots(slot, +1)

    def update_slots(self, slot, delta):
        pass

    def free_slot(self, slot):
        slot.remove_vehicle()
        self.update_slots(slot, -1)

        








