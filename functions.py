
# defining functions
def hello(a):
    print(f"hello {a}")

# calling functions
name=input("enter name:")
hello(name)



#parenthesis & arguments

def calc_area_triangle(b,h):
    area=0.5*(b*h)
    print(area)

calc_area_triangle(20,10)


#calculate area of a rectangle

def calc_area_rectangle(l,w):
    area=l*w
    print(area)

length=float(input("enter the length:"))
width=float(input("enter the width:"))
calc_area_rectangle(length,width)


#create a function
#prompt the user for a number
#whether number is even or odd

def even_odd(number):
    even=number%2==0
    print("even")

number=int(input("enter the number:"))
even_odd(number)