def fn1():
    result = x + y
    print(result)
  
def fn2():
    x = 20  # define local variable
    result = x + y
    print(result)
  
x = 10
y = 20
fn1()
fn2()
