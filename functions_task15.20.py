#task 15 to 20
# Write a program that takes input of someone's 

def calc_gross(a,b):
    gross_salary=a+b
    return gross_salary

# basic salary and  benefits,
basic_salary=int(input("Enter basic salary:"))
benefits=int(input("Enter benefits:"))
gross_salary=calc_gross(basic_salary, benefits)
print("Gross Salary:",gross_salary)

#adds them to find the gross salary then uses  the gross salary to find the nhif.

def calc_nhif(gross_salary):

    if gross_salary >= 0 and  gross_salary <= 5999:
        nhif=150
    elif   gross_salary >= 6000 and  gross_salary <= 7999:
        nhif=300
    elif   gross_salary >= 8000 and  gross_salary <= 11999:
        nhif=400
    elif   gross_salary >= 12000 and  gross_salary <= 14999:
        nhif=500
    elif  gross_salary >= 20000 and  gross_salary <= 24999:
        nhif=750
    elif  gross_salary >= 25000 and  gross_salary <= 29999:
        nhif=850
    elif  gross_salary >= 30000 and  gross_salary <= 34999:
        nhif=900
    elif  gross_salary >= 35000 and gross_salary <= 39999:
        nhif=950
    elif  gross_salary >= 40000 and gross_salary <= 44999:
        nhif=1000
    elif  gross_salary >= 45000 and gross_salary <= 49999:
        nhif=1100
    elif  gross_salary >= 50000 and gross_salary <= 59999:
        nhif=1200
    elif  gross_salary >= 60000 and gross_salary <= 69999:
        nhif=1300
    elif  gross_salary >= 70000 and gross_salary <= 79999:
        nhif=1400
    elif  gross_salary >= 80000 and gross_salary <= 89999:
        nhif=1500
    elif  gross_salary >= 90000 and gross_salary <= 99999:
        nhif=1600
    else:
        nhif=1700
    return nhif

NHIF=calc_nhif(gross_salary)
print("NHIF:",NHIF)


# Continue with the program above, then use  the gross salary to find the NSSF. 
# To find the Kenya NSSF Rate using. Compute NSSF using 6% of the Gross Salary. 
# BUT ONLY A MAXIMUM OF 18,000 CAN BE USED IN NSSF. 

def calc_nssf(gross_salary,rate=0.06):
    if gross_salary<18000:
        nssf=gross_salary*0.06
    else:
        nssf=18000*0.06
    return nssf

NSSF=calc_nssf(gross_salary)
print("NSSF:",NSSF)



# Continue with the same program and calculate an individual’s NHDF using:
#  i.e NHDF = gross_salary *  0.015

def calc_nhdf(gross_salary, rate=0.015):
    nhdf = gross_salary *  0.015
    return nhdf

NHDF=calc_nhdf(gross_salary, rate=0.015)
print("NHDF:",NHDF)

# Calculate the taxable income.

def calc_taxable_income(gross_salary):
    total_taxable_income = gross_salary - (NSSF + NHDF)
    return total_taxable_income

taxable_income = calc_taxable_income(gross_salary) 
print("Taxable income:",taxable_income)

# Continue with the same program and find the person's PAYEE using the taxable income above.

def calc_payee(taxable_income):
    if taxable_income >= 0 and taxable_income <= 24000:
        total_payee = (taxable_income * 0.01)
    elif taxable_income > 24000 and taxable_income <= 32333:
        total_payee = (taxable_income - 24000) * 0.25
    else: 
        total_payee = ((taxable_income - 32333) * 0.3) + (8333 * 0.25)
    return(total_payee)
            

payee=calc_payee(taxable_income)
print("Payee:",payee)

# Continue with the same program and calculate an individual’s Net Salary using:

def calc_deductions(h):
    total_deductions=gross_salary-(NHIF + NHDF +  NSSF + payee)
    return total_deductions


net_salary = calc_deductions(gross_salary)
print("Net Salary:",net_salary)
