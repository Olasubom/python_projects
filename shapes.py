# Create a class Person with attributes name and age, and a method greet() that prints “Hello, my name is {name}”. Create a subclass Student that inherits from Person and adds an attribute student_id. Write a method introduce() that prints the name, age, and student ID. Show how to use this subclass.


class Person:
    def __init__(self , name, age):
        self.name = name
        self.age = age 
    
    def greet(self):
         print(f"Hello my name is {self.name}")
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    
    def introduce(self):
        self.greet()
        print (f"and i am {self.age} years old , my student id is {self.student_id}")

# man = Person("ade", 40)
# man.greet()

guy = Student("ade" , 40 , 4456)
guy.introduce()


# Create a class Vehicle with attributes make and model and a method display_info() that prints the make and model. Create a subclass Car that inherits from Vehicle and adds an attribute doors. Write a method display_car_info() that prints the make, model, and number of doors and number of tires. Demonstrate the implementation.
print("")

class Vehicle:
    def __init__(self , make, model):
        self.make = make
        self.model = model
    
    def display_info(self):
        print(f"Car : {self.make}, Model : {self.model}")

class Cars(Vehicle):
    def __init__(self, make, model, doors, tires):
        super().__init__(make, model)
        self.door = doors
        self.tires = tires
    def display_car_info(self):
        self.display_info()
        print(f"Number of doors: {self.door}, Number of tires: {self.tires}")


# start_car = Vehicle("Supra", "A14")
# start_car.display_info()

show_car = Cars("Supra" , "A14", 4 , 4)
show_car.display_car_info()


# # Create a class Employee with attributes name and salary, and a method display_details() that prints the employee’s name and salary. Create a subclass Manager that inherits from Employee, adds an attribute department, and overrides the display_details() method to also print the department. Ensure the Manager class calls the display_details() method of the Employee class using super(). Demonstrate the usage of both classes.
print("")

class Employee:
    def __init__(self , name , salary):
        self.name = name 
        self.salarys = salary

    def display_details(self):
        print(f"Name: {self.name} salary: ${self.salarys}")
class Manager(Employee):
    def __init__(self, name, salary , department):
        super().__init__(name, salary)
        self.department = department
    
    def display_details(self):
        print(f"Name: {self.name} salary: ${self.salarys} Department: {self.department}")

custom = Employee("bayo" , 3400)

line = Manager("Ade" , 3400, "Computer")

for i in (custom,line):
    i.display_details()


# Create a class Shape with a method perimeter() that raises a NotImplementedError. Create subclasses Square and Triangle. The Square class should have an attribute side and override the perimeter() method to calculate the perimeter of a square. The Triangle class should have attributes a, b, and c representing the sides of the triangle and override the perimeter() method to calculate the perimeter of a triangle. Demonstrate the usage of polymorphism by iterating through a list of different shapes and calling their perimeter() methods.
print("")
class Shape:
    def perimeter():
        raise NotImplementedError()
class square(Shape):
    def __init__(self , side):
        self.side = side
    def perimeter(self):
        return self.side + self.side + self.side + self.side
class Triangle(Shape):
    def __init__(self, a ,b ,c):
        self.a = a 
        self.b = b
        self .c = c 
    def perimeter(self):
        return self.a + self.b + self.c

sqr = square(4)
tri = Triangle(2,3,4)

for i in (sqr,tri):
    print(i.perimeter())


# Create a class Person with attributes name and a method show_info() that prints the name. Create a subclass Employee that inherits from Person and adds an attribute salary, and overrides show_info() to print both name and salary. Further, create another subclass Manager that inherits from Employee and adds an attribute department. Use the super() function in Manager to call the show_info() method of Employee and add the department information.
print("")

class Person:
    def __init__(self , name):
        self.name = name
    def show_info(self):
        print(f"NAME: {self.name}")

class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary
    def show_info(self):
        print(f"NAME: {self.name} SALARY: ${self.salary}")
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    def show_info(self):
        print(f"NAME: {self.name} SALARY: ${self.salary} DEPARTMENT: {self.department}")

info_1 = Person("ADE")
info_2 = Employee("Ade", 3500)
info_3 = Manager("Ade", 3500, "COMPUTER")

for info in (info_1,info_2,info_3):
    info.show_info()



print("")


