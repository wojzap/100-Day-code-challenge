# with open("weather_data.csv") as data:
#     data = data.readlines()
#
# print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     row_counter = 0
#     for row in data:
#         row_counter += 1
#         if row_counter > 1:
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas as pd
#
# data = pd.read_csv("weather_data.csv")
# # data_dict = data.to_dict()
# # temp_list = data["temp"].to_list()
# #
# # # average temperature
# # sum_of_temperature = 0
# # for temp in temp_list:
# #     sum_of_temperature += temp
# #
# # average_temp = sum_of_temperature/len(temp_list)
# # print(average_temp)
# # print(data["temp"].mean())
# #
# # maximum temperature
# # max_temp = data["temp"].max()
# # print(max_temp)
#
# # Get data in Row
# # print(data[data.day == "Monday"])
# #
# # # print(data[data.temp == max_temp])
# #
# # monday = data[data.day == "Monday"]
# # # print(monday.condition)
# #
# # monday_temp_in_fahr = monday.temp * 1.8 + 32
# # print(monday_temp_in_fahr)
#
# # Create a dataframe from scratch
#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pd.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

squirrel_colors = data["Primary Fur Color"]
gray_squirrels = squirrel_colors.value_counts().Gray
black_squirrels = squirrel_colors.value_counts().Black
cinnamon_squirrels = squirrel_colors.value_counts().Cinnamon

squirrels_count = {
    "Color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray_squirrels, black_squirrels, cinnamon_squirrels]
}

data = pd.DataFrame(squirrels_count)

data.to_csv("squirrel_count.csv")