# Yeah so this day is about {List Comprehension},

# for starting,, lets see its syntax first

numbers  = [1, 2, 3, 4, 5, 6]
# should have something on which we can use list comprehension, it can be a list or string or something else.

# now, original line
new_numbers = [n for n in numbers if n < 5]

# [(to apply operation like multiplication addition etc...) for (i of for loop, just a name to address elements,
# must be same as the 1st) in (name of list or string or whatever you have) if (test or condition to select n from
# all elemnts or to perform any action, but not all of them only selective, seperated by a codition)]

print(new_numbers)

# answer should contain 1,2,3,4 only

squares = [n**2 for n in numbers if n < 5]   # applied operation to only those who are fulfilling the condition!!!
print(squares)


with open("num1.txt", "r") as f:
    number1 = [int(n) for n in f.readlines()]

with open("num2.txt", "r") as f:
    number2 = [int(n) for n in f.readlines()]

print(number1)
print(number2)

# numbers = number1 + number2
# print(numbers)

common = [int(n) for n in number1 if n in number2]
print(common)