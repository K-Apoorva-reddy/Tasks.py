#ENCAPSULATION-->grouping (packing) and security.
#for grouping we use classes
#for security we use access modifiers.
#There are three types of access specifiers:-
#PUBLIC--> name ->we can access  those variables in same class, thorugh object 
# without restrictions.
#-->public access modifier/public access modifier/public member
#-->if we declare an attribute in one class then we can access it anywhere in the prg.
class Sample:
    def _init_(self):
        self._name = "Appu"
obj = Sample()
print(obj._name)
# PROTECTED--> _name ->we aren't suppose to access variables outside of 
# the classs, but we can access which aren't recommanded.
class Parent:
    def _init_(self):
        self._user="Appu"
class Child(Parent):
    def _init_(self):
        super()._init_()
        print(self._user) #it is allowed
obj1 = Child()
# PRIVATE--> __name ->we can't allowed to access variables outside of the class but we can hack
# using name mangling approach (eg: classname__var) this is unprofessional way. to use professional
# way we can getter and setter which will define the same class.
# whenever we use only single class we aren't suppose to use protected varaible outside of the class/
# whenever if we do inheritence then protected variables are allowed to use in both child and parent.
class Parent:
    def _init_(self):
        self.__user = "Appu"  # private variable
class Child(Parent):
    def _init_(self):
        super()._init_()
        # Access using name mangling
        print(self.Parent_user)  # ✅ Correct way
obj1 = Child()


#getter
class Sample:
    def _init_(self):
        self.__name="Appu"
    def getDetails(self):
        return self.__name
obj=Sample()
print(obj.getDetails())

#setter
class Demo:
    def _init_(self):
        self._name = "Appu"  # Correct use of self

obj = Demo()
print(obj._dict)           # Corrected __dict_
obj._name = "Appu"         # Optional (already set in constructor)
print(obj._dict_)


#MULTIPLE CLASSES WITH INHERITENCE:-
# 1) protected(_var)-->we can allowed to access the varaible with the 
# variable with in the classes which are being inherited and allowing inheritence.
# 2) private(__var)-->as same like before in single class.

#public
class Robo:
    x=100
    def chitti(self):
        print("hai")
obj = Robo()
obj.chitti()

#
class BankAccount:
    def _init_(self, account_number, initial_balance):
        self.__account_number = account_number
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return self.__balance

    def display_account_info(self):
        masked_acc = "*" + self.__account_number[-3:]
        print(f"Account: {masked_acc}, Balance: {self.__balance}")

#
class Employee:
    def _init_(self):
        self.__name = None
        self.__salary = 0

    def set_name(self, name): 
        self.__name = name

    def set_salary(self, salary):
        if salary > 10000:
            self.__salary = salary
            print(f"{self._name}'s salary is ₹{self._salary}")
        else:
            print("Salary must be greater than ₹10,000")

    def display_employee(self):
        print("Employee Name:", self.__name)
        print("Current Salary: ₹", self.__salary)

encap method over riding
