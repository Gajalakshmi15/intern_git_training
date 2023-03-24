str1=["keerthi","uma","Nivin"]
string=''
for i in str1:
    if string=='':
        string+=i
    else:
        string=string+","+i
print(string)