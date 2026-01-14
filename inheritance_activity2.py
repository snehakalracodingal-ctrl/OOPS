class Person:
    def __init__(self,name,idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print("Name :", self.name)
        print("ID Number :", self.idnumber)
class Employee(Person):
    def __init__(self,name,idnumber,salary,post):
        Person.__init__(self,name,idnumber)
        self.salary = salary
        self.post = post
    def display(self):
        Person.display(self)
        print("Salary :", self.salary)
        print("Post :", self.post)
a=Employee("John", 886012, 20000, "Intern")
a.display()