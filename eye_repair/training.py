import time


def beep(freq, dur=100):
    import winsound
    winsound.Beep(freq, dur)


for i in range(20):
    print(i)
    if i == 9:
        beep(2000, 2000)

    beep(1000, 2000)
    time.sleep(10)

beep(3000, 2000)