# 10.Take a list of names  in the format "firstname lastname".Then make a dictionary  with key as the last name  and value as the first name.
'''
1.Take the input as list.
2.create an empty dictionary
3.By using for loop to take the elements from list
4.By using split comment to split the elements from the list
5.And give the condition .at finally print it
'''
x=["yuva shree","divya shri","siva priya","aakash geetha"]
dict={}
for i in x:
    i=i.split(" ")

    dict[i[1]]=i[0]
print(dict)


