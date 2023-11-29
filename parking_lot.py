import random

class ParkingLot:
    def __init__(self, size, spot_length=8, spot_width=12):
        self.spot_length = spot_length
        self.spot_width = spot_width
        self.total_spots = size // (spot_length * spot_width)
        self.parking_spots = [None] * self.total_spots
    
    def find_available_spot(self):
        for i, spot in enumerate(self.parking_spots):
            if spot is None:
                return i
        return None
    
    def park_car(self, car, spot):
        if self.parking_spots[spot] is None:
            self.parking_spots[spot] = car
            return f"Car with license plate {car.license_plate} parked successfully in spot {spot}"
        else:
            return f"Spot {spot} is occupied, car was not parked successfully"

class Car:
    def __init__(self, license_plate):
        self.license_plate = license_plate
    
    def __str__(self):
        return self.license_plate
    
    def park(self, parking_lot):
        available_spot = parking_lot.find_available_spot()
        if available_spot is not None:
            return parking_lot.park_car(self, available_spot)
        else:
            return "Parking lot is full, car cannot be parked"
        
def main():
    cars = [Car("ABC1234"), Car("XYZ5678"), Car("DEF9012"), Car("GHI3456")]
    parking_lot = ParkingLot(2000)  # Adjust the size of the parking lot here
    
    while cars:
        car = cars.pop(0)
        result = car.park(parking_lot)
        print(result)
        if result == "Parking lot is full, car cannot be parked":
            break

if __name__ == "__main__":
    main()
