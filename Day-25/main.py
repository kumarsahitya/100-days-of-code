# import csv
#
# with open("weather_data.csv") as data_file:
#     reader = csv.reader(data_file)
#     tempuratures = []
#     for row in reader:
#         if row[1] != "temp":
#             tempuratures.append(int(row[1]))
#
#     print (tempuratures)


import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
print(data["temp"])