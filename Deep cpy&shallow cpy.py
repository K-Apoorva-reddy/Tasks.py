# 1.shallow copy
import copy
fruits = [["apple", "banana"], ["mango", "orange"]]

shallow = copy.copy(fruits)        # shallow copy
shallow[0][0] = "grapes"           # change first element
print("Original after shallow:", fruits)
print("Shallow Copy:", shallow)

# deep copy
fruits = [["apple", "banana"], ["mango", "orange"]]  # reset list
deep = copy.deepcopy(fruits)       # deep copy
deep[1][0] = "pineapple"           # change second element
print("Original after deep:", fruits)
print("Deep Copy:", deep)


#2.import copy

numbers = [[1, 2, 3], [4, 5, 6]]

# Shallow copy
shallow = copy.copy(numbers)
shallow[1][1] = 99
print(numbers)
print(shallow)

# Deep copy
numbers = [[1, 2, 3], [4, 5, 6]]
deep = copy.deepcopy(numbers)
deep[0][2] = 77
print(numbers)
print(deep)

#3 sum all the numbers using recursion
def recursive_sum(lst):
    total = 0
    for item in lst:
        if isinstance(item, list):  
            total += recursive_sum(item)
        else:                        
            total += item
    return total

x = [1, 2, 3, [1, 2, 3], 4, 5, 6, [3, 4, 5, [2, 3, 4, [1, 2, 3]]]]

print("Sum of all numbers:", recursive_sum(x))

#4 fibonacci series using recursion
def fibonacci(n):
    if n <= 1:   
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

terms = int(input("Enter number of terms: "))

print("Fibonacci series:")
for i in range(terms):
    print(fibonacci(i), end=" ")


# these are the outputs
Original after shallow: [['grapes', 'banana'], ['mango', 'orange']]
Original after shallow: [['grapes', 'banana'], ['mango', 'orange']]
Shallow Copy: [['grapes', 'banana'], ['mango', 'orange']]
Shallow Copy: [['grapes', 'banana'], ['mango', 'orange']]
Original after deep: [['apple', 'banana'], ['mango', 'orange']]
Original after deep: [['apple', 'banana'], ['mango', 'orange']]
Deep Copy: [['apple', 'banana'], ['pineapple', 'orange']]
[[1, 2, 3], [4, 99, 6]]
[[1, 2, 3], [4, 99, 6]]
[[1, 2, 3], [4, 5, 6]]
[[1, 2, 77], [4, 5, 6]]
Sum of all numbers: 54
Enter number of terms: 5
Fibonacci series:
0 1 1 2 3
deep and shallow