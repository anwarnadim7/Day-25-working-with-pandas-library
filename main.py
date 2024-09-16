import pandas
# data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)

# avg =sum(temp_list) / len(temp_list)
# print(avg)

# print(data["temp"].mean())
# print(data["temp"].max())
#
#
# #get data in column
# print(data["condition"])
# print(data.condition)
#
# #get Data in Rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)

# Create a dataframe from scratch
# data_dict = {
#     "students":["Any","James","Angela"],
#     "scores": [76,56,65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
#
import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240916.csv")
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count =  len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrel_count)
print(red_squirrel_count)
print(black_squirrel_count)

data_dict = {
    "Fur Color" :  ["Gray", "Cinnamon", "Black"],
    "Count" : [gray_squirrel_count,red_squirrel_count,black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
