#Write a program which gets a phone number from a form input or terminal. 
# Validates the phone number 
# by checking if it starts with +254.. or 07.. or 71… or 254.. or 01... Convert the number to start with +254… 
# e.g if a user enters “0712345678”, the program should display “+254712345678”
# e.g if a user enters “0112345678”, the program should display “+254112345678”
# e.g if a user enters “712345678”, the program should display “+254712345678

phone_number=input("Enter phone number:")

if (phone_number[0:4]=="+254") and len(phone_number)==13:
   print("valid number")
elif (phone_number[0:2]=="07" and  len(phone_number)==10):
   print("+254" + phone_number[1:], "is a valid phone number")

elif (phone_number[0:2]=="71" and  len(phone_number)==9):
   print("+254" + phone_number[1:], "is a valid phone number")
           
elif (phone_number[0:2]=="01" and  len(phone_number)==10):
   print("+254" + phone_number[1:],"is a valid phone number")

elif (phone_number[0:2]=="254" and  len(phone_number)==10):
   print("+254" + phone_number[1:],"is a valid phone number")

else:
   print("Invalid number") 