'''4.Write a Python program to add three given lists using Python map and lambda.

Problem statement:
               Expected input1:
                       [1,2,3]
                       [4,5,6]
                       [7,8,9]
                Expected output1:
                       [12, 15, 18]

Pseudocode:
       start the program
       give a three user data
       create a variable
       the variable contains the lambda condition
       print the list of the elements


Python Code:
'''

l1=[1,2,3]
l2=[4,5,6]
l3=[7,8,9]
d=map(lambda a,b,c:a+b+c,l1,l2,l3)
print(list(d))