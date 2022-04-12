# def my_function():
#     global msg
#     msg = "Hello"
#     print(msg)
#     return None
# print(dir(my_function()))
# print(msg)

def my_function():
    def my_second_function():
        global msg
        msg = "Hello"
        return None
    my_second_function()
   # print(msg)
    msg = "Hello1"
    print(f"functia principala {msg}")
    return None

my_function()
print(msg)


