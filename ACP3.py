class Vehicle:
    def __init__(self, fare_per_km):
        self.fare_per_km = fare_per_km

class Bus(Vehicle):
    def __init__(self, fare_per_km, distance):
        Vehicle.__init__(self, fare_per_km)
        self.distance = distance

    def total_fare(self):
        return self.fare_per_km * self.distance

bus = Bus(10, 15)
print("Total Fare:", bus.total_fare())
