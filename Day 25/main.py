import pandas

data = pandas.read_csv("weather_data.csv")

data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list() 
c = data[data.day == "Monday"].temp
a = (c/5*9) + 32
print(a)