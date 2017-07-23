
def checkio(text):
    temp = text.split()
    if (len(temp) < 3): return False
    for i in range(len(temp)):
        if not temp[i].isdigit() and not temp[i+1].isdigit() and not temp[i+2].isdigit():
            return True
        elif i == len(temp) - 2:
            return False


# print(checkio("Hello World hello"))
# print(checkio("He is 123 man"))
# print(checkio("1 2 3 4"))
# print(checkio("bla bla bla bla"))
# print(checkio("Hi"))
print(checkio("one two 3 four five six 7 eight 9 ten eleven 12"))
# checkio("Hello World hello") == True
# checkio("He is 123 man") == False
# checkio("1 2 3 4") == False
# checkio("bla bla bla bla") == True
# checkio("Hi") == False
