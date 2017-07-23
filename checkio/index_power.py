def index_power(array, number):
    return (array[number] ** number if len(array) > number else -1)



print(index_power([1, 2, 3, 4], 2))
print(index_power([1, 3, 10, 100], 3))
print(index_power([0, 1], 0))
# index_power([0, 1], 0) == 1
print(index_power([1, 2], 3))
# index_power([1, 2], 3) == -1
print(index_power([96,92,94],3))
