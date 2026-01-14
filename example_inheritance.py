class dad:

    def __init__(self,eyes,aggression):
        self.eyes = eyes
        self.aggression = aggression
    def display(self):
        print("Eyes color :", self.eyes)
        print("Aggression level :", self.aggression)

class child(dad):
    def __init__(self,name,age,eyes,aggression):
        dad.__init__(self,eyes,aggression)
        self.name = name
        self.age = age

obj=child("Tokai",11,"Brown","Low")
obj.display()

print("Name :", obj.name)
print("Age :", obj.age)


#Subclass
class Vehicle:
    def __init__(VehicleType):
        print("Vehicle is a ", VehicleType)

class Car(Vehicle):
    def __init__(self):
        Vehicle.__init__("Car")

print(issubclass(Car,Vehicle)) 
       