#write a function that will find the avg of the temperature listed in file data.txt

def calc_avg():
    with open("data.txt", "r") as file:
        data = file.readlines()
        num_as_string = data[1:]   #as the readlines() function returns a list of of strings"
        numbers = [float(i) for i in num_as_string]
        avg = sum(numbers)/len(numbers)
        return avg

print(f"Average of the numbers: {calc_avg()}")
