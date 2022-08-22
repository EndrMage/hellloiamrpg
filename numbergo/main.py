a = 1
b = 1
print(a)
print(a)
while a <= 10000000:
    b=a+b
    c=b
    b=a
    a=c
    print(a)

#b  2
#c  2
#b  1
#a  2
#print
#b  3
#c  3
#b  2
#a  3
#
#
