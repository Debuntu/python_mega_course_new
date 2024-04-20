names = ["David", "Bipro", "Will", "Arhant"]
names.sort()         #notice that since list is mutable, we dont need to re-assign to a variable

print(names)

a = enumerate(names)       #enumerate function produces a sequence of tuples each containing (index, item).

print(list(a))

names.reverse()      # sort ascends and reverse descends
print(names)

names.insert(2, "Mack")     #to insert anew object/elemnt before a given index
print(names)

names.remove("Mack")      #removes first occurence of the given value
print(names)






