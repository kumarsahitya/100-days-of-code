import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # get Data in Columns
# print(data["condition"])
# print(data.condition)

# get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(int(monday.temp[0]) * 9/5 + 32)

# Create a dataframe from scratch
data_dict = {
    "students": ["Any", "James", "Angela"],
    "scores": [76, 56, 64],
}
data = pandas.DataFrame(data_dict)
print(data)
# data.to_csv("new_data.csv")