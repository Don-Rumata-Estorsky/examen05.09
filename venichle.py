
class Vehicle:
    def __init__(self, license_plate: str, vehicle_type: str):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type
        self.transports= []



class Car(Vehicle):
    def __init__(self, license_plate: str,):
        super().__init__(license_plate, "Car")

    def vid(self):  
        self.transports=[ 
            Car(" 228.dem  ", "Car", ),
            Car(" 111.aaa  ", "Car", ),
            Car(" 438.fas  ", "Car", )
        ]



class Motorcycle(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, "Motorcycle")

    def vidd(self):
        self.transports=[ 
            Motorcycle(" 293.gag  ", "Motorcycle", ),
            Motorcycle(" 100.lol  ", "Motorcycle", )
        ]



def end(a):
    a.vid()
    a.vidd()









