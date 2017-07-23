
def checkio(digits):
    result = 1
    for i in (list(str(digits))): result = int(i.replace("0", "1"), 10)*result
    # result = int(i.replace("0", "1"), 10)*result for i in (list(str(digits)))
    return result



print (checkio(999))
print(checkio(12340))
checkio(1000)
checkio(1111)
# checkio(123405) == 120
# checkio(999) == 729
# checkio(1000) == 1
# checkio(1111) == 1
