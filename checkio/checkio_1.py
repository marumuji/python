# array = [1, 3, 2, 1, 3]
# array = [1, 2, 3, 4, 5]
# array = [5, 5, 5, 5, 5]
array = [10, 9, 10, 10, 9, 8]
new_array = []

for i in array:
    if(array.count(i) != 1):
        new_array.append(i)

# print(array)
# print("new_array = {}".format(new_array))

print(new_array)
