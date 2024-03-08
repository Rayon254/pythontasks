# Write a program that takes input of someone's 
basic_salary=int(input("Enter basic salary:"))
benefits=int(input("Enter benefits:"))


# basic salary and  benefits,  
gross_salary=basic_salary+benefits
print("Gross Salary:", gross_salary)

#adds them to find the gross salary then uses  the gross salary to find the NHIF.
if gross_salary >= 0 and  gross_salary <= 5999:
    NHIF=150
elif   gross_salary >= 6000 and  gross_salary <= 7999:
    NHIF=300
elif   gross_salary >= 8000 and  gross_salary <= 11999:
    NHIF=400
elif   gross_salary >= 12000 and  gross_salary <= 14999:
    NHIF=500
elif  gross_salary >= 20000 and  gross_salary <= 24999:
    NHIF=750
elif  gross_salary >= 25000 and  gross_salary <= 29999:
    NHIF=850
elif  gross_salary >= 30000 and  gross_salary <= 34999:
    NHIF=900
elif  gross_salary >= 35000 and gross_salary <= 39999:
    NHIF=950
elif  gross_salary >= 40000 and gross_salary <= 44999:
    NHIF=1000
elif  gross_salary >= 45000 and gross_salary <= 49999:
    NHIF=1100
elif  gross_salary >= 50000 and gross_salary <= 59999:
    NHIF=1200
elif  gross_salary >= 60000 and gross_salary <= 69999:
    NHIF=1300
elif  gross_salary >= 70000 and gross_salary <= 79999:
    NHIF=1400
elif  gross_salary >= 80000 and gross_salary <= 89999:
    NHIF=1500
elif  gross_salary >= 90000 and gross_salary <= 99999:
    NHIF=1600
else:
    NHIF=1700
print("NHIF:",NHIF)

# Continue with the program above, then use  the gross salary to find the NSSF. 
# To find the Kenya NSSF Rate using. Compute NSSF using 6% of the Gross Salary. 
# BUT ONLY A MAXIMUM OF 18,000 CAN BE USED IN NSSF. 

if gross_salary<18000:
    NSSF=gross_salary*0.06
else:
    NSSF=18000*0.06
print("NSSF:",NSSF)


# Continue with the same program and calculate an individual’s NHDF using:
#  i.e NHDF = gross_salary *  0.015

NHDF = gross_salary *  0.015
print("NHDF:",NHDF)

# Calculate the taxable income.

taxable_income = gross_salary - (NSSF + NHDF) 
print("Taxable income:",taxable_income)

# Continue with the same program and find the person's PAYEE using the taxable income above.

if taxable_income >= 0 and taxable_income <= 24000:
    payee = (taxable_income * 0.01)
elif taxable_income > 24000 and taxable_income <= 32333:
    payee = (taxable_income - 24000) * 0.25
else: 
    payee = ((taxable_income - 32333) * 0.3) + (8333 * 0.25)
print("Payee:",payee)
            

# Continue with the same program and calculate an individual’s Net Salary using:
total_deductions=NHIF + NHDF +  NSSF + payee
net_salary = gross_salary - total_deductions
print("Net Salary:",net_salary)

