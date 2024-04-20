feet_inches = input("Enter feet and inches: ")
def convert(feet_inches):
    feet_inch_list = [int(i) for i in feet_inches.split(" ")]    #we are asking to split the string at character " " in the input (for example "5 7", so we get a list [5, 7]
    meter = 0.3048*feet_inch_list[0] + 0.0254*feet_inch_list[1]
    return meter

result = convert(feet_inches)

if result < 1:
    print("Kid is too small to slide")
else:
    print("Kid can slide")