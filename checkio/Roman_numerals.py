def checkio(data):
    conversion_table =  [
        ["","I","II","III","IV","V","VI","VII","VIII","IX"],
        ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"],
        ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"],
        ["","M","MM","MMM"]
    ]

    data = [int(i) for i in (reversed(list(str(data))))]
    return "".join(reversed([conversion_table[i][data[i]] for i in range(len(data))]))








print(checkio(30))
print(checkio(19))
print(checkio(6))
print(checkio(76))
print(checkio(13))
print(checkio(44))
print(checkio(3999))
# checkio(6) == 'VI'
# checkio(76) == 'LXXVI'
# checkio(13) == 'XIII'
# checkio(44) == 'XLIV'
# checkio(3999) == 'MMMCMXCIX'
