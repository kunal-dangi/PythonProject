class Cars:

    def __init__(self, engines):

        # __init__ is a constructor which can be called automatically whenever  an object is created but can also be
        # created manually even we can pass some initial characters !!!!!  {pretty Awesome right?}

        # Here i have written (self) as the first parameter ,, not my choice more like a syntax!!!!
        # Have to make self the first parameter of any method or function,,,,  {How to use it??.. Let's see}

        self.engines = engines

        def start(self):
            pass

        def drink(self):
            pass
        # basic syntax to write or declare functions/methods in a class

        # Let's say you don't wanna use "self" what then??
        # We use @staticmethod to write a method on a class level,,, and noo need to write self in it {But have to use
        # for everything else}

        # Like ->

        @staticmethod
        def Eat(eating):
            return eating


        # INHERITANCE    {One of Major things that are important in OOPS!!!!!}
        #Syntax ->
        #Parent Class Firstly:
        class Animals:
            def __init__(self, name, age):
                self.name = name
                self.age = age

        # all the methods in Parent Class can be used in Child class
        #Child class lastly:
        class Dog(Animals):
            def __init__(self, name, age):
                super().__init__(name, age)



        # Now, To use Access Specifiers in Python,, we have to use some special signs!!
        # use `__` before every attribute or method to make it private!! {Pretty simple right?}

        class Access:
            def __main(self, __private):
                self.__private = __private
            # both function "main" and attribute "private" are private
            def main(self, public):
                self.public = public
            # both function "main" and attribute "public" are public




# Lets get an example of Inheritance!!

    class Car:
        color="Black"
        def __init__(self, engine=None):
            self.engine = engine
        @staticmethod
        def Start():
            print("Car Started..!!!")

        @staticmethod
        def Stop():
            print("Car Stopped.!!")

    class Toyota(Car):
        def __init__(self, name, model, engine=None):
            super().__init__(engine)
            self.name= name
            self.model = model

    car1= Toyota("Fortuner", "ZXL")
    car2= Toyota("Supra", "M4")
    print(car1.name, car1.model)
    print(car2.name, car2.model)
    print(car1.color)





# Dunder Functions ^_^

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def ShowNumber(self):
        print(self.real, "i + ", self.img, "j")

    def __add__(self, other):                   # Dunder Function BBY
        newReal = self.real + other.real
        newImg = other.img + other.img
        return Complex(newReal, newImg)


num1 = Complex(1,4)
num1.ShowNumber()
num2 = Complex(2,3)
num2.ShowNumber()

num3 = num1 + num2

num3.ShowNumber()