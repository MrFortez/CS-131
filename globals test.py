def F(a):
    x = 10
    x *= a

def G(b):
    global x
    x += b

def H(c):
    global x
    x-=c

x = 100
y = 25
F(5)
G(y)
H(-25)
print(x)