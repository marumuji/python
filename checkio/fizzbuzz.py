def checkio(number):
    if(number % 3 == 0 and number % 5 == 0):
        return "Fizz Buzz"
    elif(number % 3 == 0):
        return "Fizz"
    elif(number % 5 == 0):
        return "Buzz"
    else:
        return number

print (checkio(15))
print (checkio(3))
print (checkio(5))
print (checkio(7))
print (checkio(8340))
