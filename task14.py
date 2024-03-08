# Write a program that takes input of 2 values and adds them. The program should only accept 
# numbers
#  and floats only or otherwise display an error “invalid character entered”
#  and take the user to re-enter the inputs .

input1=input("Enter number:")
input2=input("Enter number:")

if '.' in input1 and '.' in input2:
    input1=float(input1) 
    input2=float(input2)

    sum=input1+input2
    print(sum)
else:
    print("Invalid character entered")
    print("Re-enter")
