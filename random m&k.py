#Generate 5 random floats between 0 and 1.
import random
for i in range(5):
    print(random.random())

#Dice roll simulator using random.randint.
import random
dice = random.randint(1, 6)
print(dice)

#Convert 90 degrees to radians.
import math
degrees = 90
radians = math.radians(degrees)
print(radians)

#factorial of a user-given number
import math
a=int(input("Enter a number:"))
print(math.factorial(a))

#Shuffle a list of 10 integers.
import random
list=[1,2,3,4,5]
random.shuffle(list)
print(list)

#Calculate Compound Interest using math.pow
import math
principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate (in %): "))
time = float(input("Enter time in years: "))
amount = principal * math.pow((1 + rate / 100), time)
print("Compound Interest Amount is:", round(amount, 2))

#Trigonometry Calculator using Degrees
import math
degree = float(input("Enter angle in degrees: "))
radian = math.radians(degree)
print("sin({}) = {}".format(degree, round(math.sin(radian), 4)))
print("cos({}) = {}".format(degree, round(math.cos(radian), 4)))
print("tan({}) = {}".format(degree, round(math.tan(radian), 4)))
