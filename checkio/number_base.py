def checkio(*args):
    try:
        return int(args[0], args[1])
    except:
        return -1


print(checkio("AF", 16))
print(checkio("101", 2))
print(checkio("101", 5))
print(checkio("Z", 36))
print(checkio("AB", 10))
# checkio("AF", 16) == 175
# checkio("101", 2) == 5
# checkio("101", 5) == 26
# checkio("Z", 36) == 35
# checkio("AB", 10) == -1
