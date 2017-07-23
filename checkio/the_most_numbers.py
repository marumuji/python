def checkio(*data):
    if len(data) == 0:
        return 0
    return round(max(data) - min(data), 3)



print(checkio(1, 2, 3))
print(checkio(1))
print(checkio(5, -5))
print(checkio(10.2, -2.2, 0, 1.1, 0.5))
print(checkio())
print(checkio(-0.036,-0.11,-0.55,-64))

# checkio(1, 2, 3) == 2
# checkio(5, -5) == 10
# checkio(10.2, -2.2, 0, 1.1, 0.5) == 12.4
# checkio() == 0
