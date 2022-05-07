import time

# https://www.youtube.com/watch?v=Ox31h9EEYT0
# https://www.youtube.com/watch?v=_DnHa-L3wug
# https://www.youtube.com/watch?v=HvU3g3M0fcs

def beep(freq, dur=100):
    import winsound
    winsound.Beep(freq, dur)

print("Input number of times: ", end='')
num = int(input())

for i in range(num):
    print(i, " times")
    for j in range(20):
        print(j, flush=True)
        if j == 9 or j == 19:
            beep(5000, 2000)
        elif j == 6 or j == 16:
            beep(2000, 1000)
        elif j == 7 or j == 17:
            beep(3000, 1000)
        elif j == 8 or j == 18:
            beep(4000, 1000)
        elif j < 6:
            beep(750, 1000)
        elif 9 < j and j < 16:
            beep(1000, 1000)
        time.sleep(1)

beep(3000, 2000)
print("finish")
