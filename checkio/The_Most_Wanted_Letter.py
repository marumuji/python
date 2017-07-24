def checkio(args):
    result = None
    for i in range(97, 97+26):
        if result == None:
            result = chr(i)
        elif args.lower().count(result) < args.lower().count(chr(i)):
            result = chr(i)
    print(result)


checkio("Hello World!")
checkio("How do you do?")
checkio("One")
checkio("Oops!")
checkio("AAaooo!!!!")
checkio("abe")

# checkio("Hello World!") == "l"
# checkio("How do you do?") == "o"
# checkio("One") == "e"
# checkio("Oops!") == "o"
# checkio("AAaooo!!!!") == "a"
# checkio("abe") == "a"
