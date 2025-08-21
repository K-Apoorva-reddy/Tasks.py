#Add all elements of a list.
numbers = [5, 10, 15, 20]
total = sum(numbers)
print("Sum of list elements is:", total)

#Find max and min in a list.
list=[34,89,38,29]
print(min(list),max(list))

#Count even and odd numbers in a list.
numbers = [1, 4, 7, 10, 13, 16, 19]
even_count = odd_count = 0
for num in numbers:
    even_count += (num % 2 == 0)
    odd_count += (num % 2 != 0)
print("Even:", even_count, "Odd:", odd_count)

#Reverse a list without using reverse().
numbers = [1, 2, 3, 4, 5]
reversed_list = numbers[::-1]
print("Reversed List:", reversed_list)

#. Remove duplicates from list.
#numbers = [1, 2, 2, 3, 4, 4, 5]
#unique_numbers = list(set(numbers))
#print(unique_numbers)

#Sort a list of strings by length.
words = ["apple", "banana", "kiwi", "grape"]
sorted_words = sorted(words, key=len)
print("Sorted by length:", sorted_words)

#Find the second largest number in the list.
numbers = [5, 8, 1, 10, 7]
sorted_numbers = sorted(numbers, reverse=True)
second_largest = sorted_numbers[1]
print("Second Largest Number is:", second_largest)

#Check if two lists are equal
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)

# Merge two lists and sort them
a = [3, 1, 4]
b = [2, 5]
merged = sorted(a + b)
print(merged)

# Convert tuple to list and back
#tuple = (1, 2, 3)
#list = list(tuple)
#tup = tuple(list)
#print(list,tup)

#Check if tuple contains a value
t = (1, 2, 3, 4)
print(3 in t)  

#Unpack a tuple into variables
t = (1, 2, 3)
a, b, c = t
print(a, b, c)

#Count how many times a number appears in a list
nums = [1, 2, 2, 3, 2]
print("2 appears:", nums.count(2), "times")

# Create list of squares using comprehension
squares = [x**2 for x in range(1, 6)]
print(squares)

#Find index of element in tuple
t = (5, 3, 7)
print(t.index(7))

# Slice a tuple from index 1 to 3
t = (1, 2, 3, 4, 5)
print("Sliced tuple:", t[1:4])

#Replace element in list with another
lst = [1, 2, 3, 4]
lst[2] = 99
print(lst)

#Filter only strings from a mixed list
mixed = [1, 'apple', 3.5, 'banana']
strings = [x for x in mixed if isinstance(x, str)]
print(strings)

#Take list input from user and print sum
#lst = list(map(int, input("Enter numbers separated by space: ").split()))
#print("Sum is:", sum(lst))
