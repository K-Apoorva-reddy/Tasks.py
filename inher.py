#---acquring methods,behaviour ad attributes from already defined class into newly created.
#---class is called inheritence.
#---creating new class from already created class
#types of inheritence:-
#--->single:-
#---if we derive one child class from single parent class then it is a single inheritence.
#---it have one base class and one derived class
#syntax:-
#   class baseclass:
#   class derived-class(baseclass):
#--->mutiple:-
#---if we derive one child class from more than one parent class then it is multiple inheritence.
#--->multi level
#--->hierarchical
#--->hybrid

# 1) wap to implement single inheritence
class robo:
    def one(self): 
        print("this is base class")
class chitti(robo):
    def two(Self):
        print("this is derived class")
#object creation happening
obj = chitti()
obj.one()
obj.two()

# 2) single inheritence
class Parent:
    def Pmethod(self):
        print("i am a method from parent")
    def Pmethod2(self):
        print("i am a second method from parent")

class Child(Parent):
    def Cmethod(self):
        print("i am a method from child")
        super().Pmethod2() #calling method from super class using super()

obj1=Child()
obj1.Cmethod()
obj1.Pmethod()
obj1.Pmethod2()

# 3)
class User:
    def _init_(self, name, email):
        self.name = name
        self.email = email
class Student(User):
    def _init_(self, name, email, enrolledcourses):
        super()._init_(name, email)
        self.enrolledcourses = enrolledcourses
    def getCourses(self):
        print(f"{self.name} is learning {self.enrolledcourses}")
class Instructor(User):
    def _init_(self, name, email, courses_training):
        super()._init_(name, email)
        self.courses_training = courses_training
    def getCourses(self):
        print(f"{self.name} is teaching {self.courses_training}")
# Creating student object
Student_obj = Student("Deepthi", "deepthi@gmail.com", ["HTML", "CSS", "Python", "JS"])
Student_obj.getCourses()
# Creating instructor object
Trainer_obj = Instructor("Harish", "harish@gmail.com", ["Frontend", "Backend", "DB", "AI"])
Trainer_obj.getCourses()

#4)
class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age
    def display_person(self):
        print(f"Name: {self.name}, Age: {self.age}")
class Employee(Person):  # Single inheritance
    def _init_(self, name, age, emp_id):
        super()._init_(name, age)  # calling parent constructor
        self.emp_id = emp_id
    def display_employee(self):
        print(f"Employee ID: {self.emp_id}")
# Create an employee object
e = Employee("Deepu", 22, "EMP123")
# Access parent and child methods
e.display_person()
e.display_employee()

#5)
class Animal:
    def _init_(self, name):
        self.name = name
    def speak(self):
        print("Animal makes a sound")
class Dog(Animal):
    def bark(self):
        print(f" {self.name} is barking") 
d1 = Dog("tommy")
d1.speak()
d1.bark()

#6)
class Vehicle:
    def _init_(self, brand):
        self.brand = brand
    def show_brand(self):
        print(f"Brand name: {self.brand}")
class Car(Vehicle):
    def _init_(self, brand, model):
        super()._init_(brand)  # calling parent constructor
        self.model = model
    def show_details(self):
        print(f"Brand: {self.brand}, Model: {self.model}")
# Create an object of Car
car1 = Car("Honda", "City")
car1.show_brand()
car1.show_details()

#7)
class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def _init_(self, name, age, college):
        super()._init_(name, age)  # Initialize name and age from parent
        self.college = college       # Add college info

    def display_student(self):
        print(f"Name: {self.name}, Age: {self.age}, College: {self.college}")

# Create a student object
s1 = Student("Deepthi", 21, "CMR Engineering College")

# Call methods
s1.display_person()     # From parent class
s1.display_student()    # From child class


# 8) A class Teacher with:Attribute: subject
#Method: teach() → prints: "Teaches <subject>"
#A class SportsCoach with:
#Attribute: game
#Method: coach() → prints: "Coaches <game>"
#A class TeacherCoach that inherits from both Teacher and SportsCoach
#Method: details() → prints both subject and game.
class Teacher:
    def _init_(self, subject):
        self.subject = subject

    def teach(self):
        print(f"Teaches {self.subject}")

class SportsCoach:
    def _init_(self, game):
        self.game = game

    def coach(self):
        print(f"Coaches {self.game}")

class TeacherCoach(Teacher, SportsCoach):
    def _init_(self, subject, game):
        Teacher._init_(self, subject)
        SportsCoach._init_(self, game)

    def details(self):
        print(f"Subject: {self.subject}, Game: {self.game}")

# Create object
t1 = TeacherCoach("Math", "Basketball")

# Call methods
t1.teach()       # From Teacher
t1.coach()       # From SportsCoach
t1.details()     # From TeacherCoach

# 9)
class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def _init_(self, name, age, student_id):
        super()._init_(name, age)  # Call base class constructor
        self.student_id = student_id

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}")

# Create object
s1 = Student("Deepu", 21, "S1024")
print()
s1.display_info()
inheritence