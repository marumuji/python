def safe_pawns(pawns):
    list_pawns = list(pawns)
    count = 0
    for i in list_pawns:
        if list_pawns.count(chr(ord(i[0])-1) + str(int(i[1])-1)) + \
           list_pawns.count(chr(ord(i[0])+1) + str(int(i[1])-1)):
             count = count + 1
    print(count)

    #    char = list(i)
    #    raw = ord(char[0])
    #    col = int(char[1])
    #    if raw != 97:
    #        raw = raw - 1
    #    if col != 1:
    #        col = col -1
    #    print(chr(raw)+str())
    #    print(array.count(chr(raw) + str(col)))



safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"})
safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) 
# safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"})
# safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
# safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
