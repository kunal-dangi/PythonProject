# #with open("225 weather-data.csv", "r") as data:
# #    data = data.read()
# #    data= data.split()
# #    print(data)
#
# # for making simple list of csv's data
#
# # import csv
# #
# # temperature = []
# #
# # with open ("225 weather-data.csv", "r") as data:
# #     data = csv.reader(data)
# #     for row in data:
# #         if row[1] != "temp":
# #             temperature.append(int(row[1]))
# #     print(temperature)
#
# # for getting each data entry in a list itself not as an element of big list
#
#
# import pandas
# import pandas as pd
#
# data = pandas.read_csv("225 weather-data.csv")
# print(data)
# print(data["temp"])
#
# data_dict = data.to_dict()
# #print(data_dict)
# # converts data to a dictionary
#
# # temp_list = data["temp"].to_list()
# #  creates a list of only temperature values
# # summation = 0
# # for i in range(len(temp_list)):
# #     x = temp_list[i]
# #     summation += x
# #
# # print(summation/len(temp_list))
#
# ## ye hai aam zindagi!!
# #
# # print(data["temp"].mean())
# # ## ye hai PANDAS Zindagi!!! Lazy as shit
# #
# # print(data["temp"].max())  # to get maximum value, come on you are not that dumb are you??
#
#
#
# # to get a row instead of a coloumn...
#
# print(data[data.day == "Monday"])
#
# # in data.day python is handling the data as an object and in data["temp"] it is behaving as a dictionary
#
#
# print(data[data.temp == data.temp.max()])
#
#
# monday = data[data.day == "Monday"]
# #how to get specific data in a more clear, standard way>>
# print(monday.temp)
#
# # to create a data_frame from scratch
#
# data_frame = {
#     "students" : ["Deepak", "Mohit", "Tanuj"],
#     "score" : [19, 20, 15]
# }
#
# Data = pd.DataFrame(data_frame)
#
# Data.to_csv("new_data.csv")



import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260904.csv")

Gray_squirrels  = len(data[data["Primary Fur Color"] == "Gray"])
Cinnamon_squirrels  = len(data[data["Primary Fur Color"] == "Cinnamon"])
Black_squirrels  = len(data[data["Primary Fur Color"] == "Black"])

print(Gray_squirrels, Cinnamon_squirrels, Black_squirrels)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [Gray_squirrels, Cinnamon_squirrels, Black_squirrels]
}

Data = pd.DataFrame(data_dict)
Data.to_csv("Data.csv")