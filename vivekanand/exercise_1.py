'''
write a script to declare two numbers.
Print True if the first number is divisible by second number.
Print False otherwise
'''
num1=int(input("enter the first number : "))
num2=int(input("enter the second number : "))

if(num1 >0 and num2 >0):
    print("True") if(num1%num2==0) else print("False")
else:
    print("Try again with a positive number...!")