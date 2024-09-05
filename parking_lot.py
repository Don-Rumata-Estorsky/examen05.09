
from venichle import Car, Motorcycle, Vehicle, end

class ParkingLot:
    def __init__(self, car_spots: int, motorcycle_spots: int):
        self.car_spots = car_spots
        self.motorcycle_spots = motorcycle_spots
        self.parked_vehicles = []

    def park_vehicle(self, vehicle: Vehicle, Car  ):
        
        
        if self.car_spots < Car.transports.__len__():
            print("нет мест для машин")
        else: 
            print("машина припаркована")
            #self.car_spots -=1


        if self.motorcycle_spots < Motorcycle.transports.__len__():
            print("нет мест для мотоциклов")
        else:
            print("мотик припаркован")
            #self.motorcycle_spots-=1


            if  self.car_spots > Motorcycle.transports.__len__():
              print("свободных парковочных мест для мотоциклов нет, вы будите расположены на автомобильную парковку, но плата больше ")
            else:
                print("нет мест для мотоциклов")
                #self.motorcycle_spots -= 1

    # Реализация метода для парковки автомобиля или мотоцикла
    def remove_vehicle(self, license_plate: str, Vehicle):
    # Реализация метода для удаления транспортного средства с парковки
        if Vehicle.vehicle_type == "Car" :
            #self.car_spots += 1
            print(f"Пипелац под номером: {license_plate} покинул своё парковочное место")
        else: 
            #self.motorcycle_spots += 1
            print(f"Мотоцикл под номером: {license_plate} покинул своё парковочное место")



    def get_parked_vehicles(self, license_plate: str):
        print(f" все припаркованные машины: ")
        for i in Car.transports.__len__():
            print( i )

        print(f" все припаркованные мотики: ")
        for i in Motorcycle.transports.__len__():
            print( i )


def itog():
    
    Car.park_vehicle()
    Motorcycle.park_vehicle()
    Car.remove_vehicle()
    Car.get_parked_vehicles()
    Motorcycle.get_parked_vehicles()


def eend():
    itogg = itog()
    itogg.end()


