# Write a program input a password. Give them only 4 attempts to check the passwords entered against “admin@123”.
#  If the password is correct access is granted. 
# After you show them a message , the account is blocked.


attempts=4
for i in range(1,5):
    password=input("Enter password:")
    if (password == "admin@123"):
        print("access is granted")
        break
    else:
        remaining_attempts=attempts-1
        if remaining_attempts>0:
            print("Try Again")
        else:
            print("the account is blocked")