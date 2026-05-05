#write a program to find out addition and difference of two numbers by creating a useer defined function.
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
sum_result=add(num1,num2)
sub_result=subtract(num1,num2)
print("addition=",sum_result)
print("subtraction=",sub_result)

#output:
""" Enter first number: 10
# Enter second number: 4
# Addition = 14
# Subtraction = 6"""
    