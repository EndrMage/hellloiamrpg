a = 1
b = 1
for a in range(0, 1001):
    b = a + b
    c = b
    b = a
    a = c
    print(a)
