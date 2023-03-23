"""   ASCII CONVERSTION    """

x="kumar"
l=[]
for i in x:
    for j in range(0,256):
        if chr(j)==i:
            l.append(j)
print(l)
