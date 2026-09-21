# # File not Found Error
# with open("notexist.txt", "r") as f:
#     f.read()
# ## this will through an error of FileNotFound
#
# #KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_exsiting_key"]
#
# #IndexError
# Class = ["IT_A","IT_B","IT_C"]
# error_class = Class[3]
#
# #Type error
# Text = "abc"
# print(Text + 5)

#well now let's start Error Handling->
# 4 terms to use; try,except,else,finally

# try:
#     file = open("data.txt", "r")
# except:                                 # never to use except directly!!!!!!!!!!! because it will switch from try to
#                                           except even if only one error is thrown in try block leaving all other
#                                           applications or algorithm in the try block completely useless
#     print("File not found")
# else:
#     input1 = file.read()
# finally:
#     print("File closed")


try:
    file = open("data.txt")
    a_dict = {"key":"value"}
    print(a_dict["key"])
except FileNotFoundError:
    file = open("data.txt","w")
    file.write("Something")
except KeyError:
    print(f"the key {a_dict['key']} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File closed")


# Raising own exception->

height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 5:
    raise ValueError("Height of a human should be less than 5!!")

bmi = weight / (height ** 2)
print(bmi)