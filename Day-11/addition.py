
# x = list(map(int,input("Enter a number: ").strip().split()))
#
# def add(*args):
#     summation = 0
#     for n in args:
#         summation += n
#     return summation
#
# lx = add(x)
# print(lx)

# so that's it for *args!!
# basically it help us to take input arguments till the user's heart's content, no hardcoded values

# Now moving on **kwargs... stands for keyword arguments,
# syntax

# def calculate(**kwargs):
#     print(kwargs)
#     summation = 0
# so basically kwargs act as a dictionary, so we need to give it atleast 2 factors... key and value

    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
#     print(kwargs["add"])
#
# calculate(add= 3, multiply= 5)

class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]

my_car = Car(make="Toyota", model="Ford")

print(my_car.make, my_car.model)

# if we have defined any function in kw and don't give it a default value... error!!!!
# if you don't want to end up with an error and want the function to get a default none value automatically,
# use kw.get() instead of kw[]

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car2 = Car(make="Nissan")
print(my_car2.make, my_car2.model)
# got model as none auto atically!!!

