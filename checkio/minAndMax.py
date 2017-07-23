def min_or_max(args, key, flg):
    result = None

    # print("args= {} key = {} len(args) = {} flg = {}".format(args, key, len(args), flg))

    if(len(args) == 1):
        result = sorted(args[0], key = key)
        if flg == max:
             return result[-1]
        else :
             return result[0]
    else :
        for arg in args:
            if result == None:
                result = arg
            elif key == None:
                if flg == max and result < arg:
                    result = arg
                if flg == min and result > arg:
                    result = arg
            elif flg == max and key(result) < key(arg):
                result = arg
            elif flg == min and key(result) > key(arg):
                result = arg
    return result


def min(*args, **kwargs):
    key = kwargs.get("key", None)
    print(min_or_max(args, key, min))
    return (min_or_max(args, key, min))

def max(*args, **kwargs):
    key = kwargs.get("key", None)
    print(min_or_max(args, key, max))
    return (min_or_max(args, key, max))


max(3, 2)
min(3, 2)
max([1, 2, 0, 3, 4])
min("hello")
max(2.2, 5.6, 5.9, key=int)
min([[1,2], [3, 4], [9, 0]], key=lambda x: x[1])

# max(3, 2) == 3
# min(3, 2) == 2
# max([1, 2, 0, 3, 4]) == 4
# min("hello") == "e"
# max(2.2, 5.6, 5.9, key=int) == 5.6
# min([[1,2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0]
