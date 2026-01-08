class Dog:
   
    animal = "Dog"

   
    def __init__(self, breed, age):
        self.breed = breed   
        self.age = age      

 
    def display_details(self):
        print("Animal:", Dog.animal)
        print("Breed:", self.breed)
        print("Age:", self.age)
        print("-------------------")


print("Creating Dog objects...\n")
dog1 = Dog("Labrador", 3)
dog2 = Dog("German Shepherd", 5)

dog1.display_details()
dog2.display_details()

print("Accessing class attribute using class name:")
print(Dog.animal)