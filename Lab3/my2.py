a = 5
b = 6
def f():
    global a, b
    c = a + b
    print (c)

f()