Fruits = ["Apples", "Oranges", "Bananas"]

def make_pie(index):
    try:
        Fruit = Fruits[index]
    except IndexError:
        print("Fruit Pie")
    else:
        print(Fruit + "pie")

make_pie(4)