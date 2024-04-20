"""
In this program we will modify the bonus_feet_inch_to_m.py to return both numbers and string in a function and
 then we will parse that to use in another function.
"""
feet_inches = input("Enter feet and inches: ")

def parse(feet_inches):
    feet_inch_list = [int(i) for i in feet_inches.split(" ")]
    feet = feet_inch_list[0]
    inch = feet_inch_list[1]
    return {"feet": feet, "inch": inch}

parsed = parse(feet_inches)       #will create a dict like {'feet': 5, 'inch': 7}

def convert(parsed):
    meter = 0.3048*parsed["feet"] + 0.0254*parsed["inch"]
    return meter

result = convert(parsed)

if result < 1:
    print("Kid is too small to slide")
else:
    print("Kid can slide")

