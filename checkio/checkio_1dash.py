# http://docs.python.jp/3/reference/compound_stmts.html#for

# array = [1, 2, 3, 2, 3]
# array = [1, 2, 3, 4, 5]
array = [10, 9, 10, 10, 9, 8]

for x in array[:]:
    if(array.count(x) == 1):
        array.remove(x)

print(array)
