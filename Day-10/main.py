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

# # that's all for now!!





# Well now lets look at {Dictionary Comprehension}
# syntax
import random

students = ["Alex", "Steve", "Gork","Ladiaz", "Stu"]

scores= {item:random.randint(1, 100) for item in students }
# assigning random score to items of list students and finally it will return in a dictionary as we have item already
# and have generated its value already, also covered in {},
#so...
print(scores)
student_dict = {student:score for student, score in scores.items()}
print(student_dict)

# output -> {'Alex': 58, 'Steve': 33, 'Gork': 45, 'Ladiaz': 86, 'Stu': 21}

# to loop through each row in data, we have a method in pandas
# its syntax is like ->
import pandas as pd
student_list = list(student_dict.items())
student_data_frame = pd. DataFrame(student_dict)
print(student_data_frame)
# actual line of looping
for (index, row) in student_data_frame.iterrows():     # iterrows()... method for looping of rows in pandas
    print(row.student, row.score)