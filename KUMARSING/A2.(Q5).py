a=""
c=int(input("enter the number of strings:"))
for i in range(c):
    inp=input("enter the string:")
    a=a+","+inp
print(a[1:])
