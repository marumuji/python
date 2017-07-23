def left_join(args):
    data = []
    for i in args : data.append(i.replace("right", "left"))
    return ",".join(data)

    # data = ','.join(list(args))
    # data = list(args)
    # print(data)


print(left_join(("left", "right", "left", "stop")))
print(left_join(("bright aright", "ok")))
print(left_join(("brightness wright",)))
print(left_join(("enough", "jokes")))
# left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
# left_join(("bright aright", "ok")) == "bleft aleft,ok"
# left_join(("brightness wright",)) == "bleftness wleft"
# left_join(("enough", "jokes")) == "enough,jokes"
