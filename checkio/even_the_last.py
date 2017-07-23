def checkio(array):
    if len(array) == 0:
        return 0
    else:
        temp = [array[x] for x in range(len(array)) if x%2==0]
        return sum(temp)*array[-1]
    #return (x+=x for x in range(array) if )


print(checkio([0, 1, 2, 3, 4, 5]))
print(checkio([1, 3, 5]))
print(checkio([6]))
print(checkio([]))

# checkio([0, 1, 2, 3, 4, 5]) == 30
# checkio([1, 3, 5]) == 30
# checkio([6]) == 36
# checkio([]) == 0
