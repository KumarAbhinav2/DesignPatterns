Design thought process:

1) A parking lot with the name and address
2) Parking lot may have multiple parking levels
3) Each Parking level will have multiple slots
4) Each slot can be of varied type - single, handicapped, LMV and Trucks/Buses
5) Each Level will have some display to show occupied and free slots
6) Each level will have Entrance and Exit
7) We may have Parking attendant and portal he is using
8) Multiple payment option like cash and credit

Classes:

1) Parking lot : Attributes: Name , Address
                 Methods: addLevel, addEntrance, issueParkingTkt, isFull
                 
2) Parking Level: Attributes: id
                    Methods: addSlot, showDisplay

3) Parking Slot: Attributes: id, type
                 Methods: 
                 
4) Parking Rate: Attributes: hr, rate

5) DisplayBoard: Attributes: id, singleSlot, handicappedSlot, lmvSlot, hmvSlot, electricSlot, 
                 Methods: showEmptySlot
                 
6) EntranceKiosk: Attributes: id
                  Methods: printTicket

6) ExitKiosk:     Attributes: id
                  Methods: scanTicket, processTicket
                  
7) Parking Attendant Portal: Attributes: id
                  Methods: scanTicket, processPayment
                  
8) Vehicle: Attributes: licenseNo, type
                  Methods: assignTicket
                  
       