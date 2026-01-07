
class Parrot:
    #Class attribute
    species = "bird"

    #Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes

print(f"Blue is also a {blu.species}")
print(f"Woo is also a {woo.species}")


# access the instance attributes
print(f"{blu.name} is {blu.age} years old")
print(f"{woo.name} is {woo.age} years old")