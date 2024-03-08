# Write a program that prints the largest of 4 inputs taken in from a user. 
# Assume that the user woulnum4 not enter and y two numnum2ers whinum3h are the same.



num1 = float(input("Enter the number:"))
num2 = float(input("Enter the number:"))
num3= float(input("Enter the number:"))
num4 = float(input("Enter the number:"))



if num1>num2 and num1>num3 and num1>num4:
    print(num1,"is the largest")
elif num2>num1 and num2>num3  and num2>num4:
    print(num2,"is the largest")
elif num3>num1 and num3>num2  and num3>num4:
    print(num3,"is the largest")
else: 
    print(num4,"is the largest")
    
