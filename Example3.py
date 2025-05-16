def f():
    global x
    x = x + 1
    print(x)

x = 5
f()
print(x)
