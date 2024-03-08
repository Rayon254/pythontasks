
#celsius to Farenheit
def celsius_to_faren(celsius):
   temp_faren=(celsius*1.8)+32
   return temp_faren

celsius=int(input("enter temp:"))
temp_faren=celsius_to_faren(celsius)
print(temp_faren)


#reverse string

def reverse_string(string):
    new_string=(string [::-1])
    return new_string

string=input("enter text:")
new_string=reverse_string(string)
print(new_string)

#number to square
def calc_square(number):
    new_number=number*number
    return new_number


number=int(input("enter the number:"))
new_number = calc_square(number)
print(new_number)
