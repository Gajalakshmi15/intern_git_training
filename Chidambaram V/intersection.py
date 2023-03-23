'''1.Write a Python program to find the intersection of two given list using Lambda.
Problem statement:
               Expected input1:
                       a=[11,21,13,41,51]
                       b=[10,20,13,40,50]
                Expected output1:
                        13

Pseudocode:
      start the program
      give two user input
      create a variable assign lambda func
      the another variable contains the set of user data
      print the elements

Python Code:'''


a=[11,21,13,41,51]
b=[10,20,13,40,50]
common=lambda x,y:x&y
l=[set(a),set(b)]
print(*(common(l[0],l[1])))
