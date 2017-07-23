# http://qiita.com/HajimeKawahara/items/02c288667f0a893e8761
def find_message(message):
    # temp = []
    # temp = [i for i in message if i.isupper()]
    return "".join([i for i in message if i.isupper()])
    # print("".join(temp))

print(find_message("How are you? Eh, ok. Low or Lower? Ohhh."))
# find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO"
print(find_message("hello world!"))
# find_message("hello world!") == ""
