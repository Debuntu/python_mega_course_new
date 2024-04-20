import csv

with open("file/testfile.csv", 'r') as file:
    data = list(csv.reader(file))


print(data)
city = input("Enter a city: ")

for item in data[1:]:    #as the first item will be ['City', ' "Temperature (F)"'], we are exluding that from iteration by slicing
    if item[0] == city:
        print(item[1])

