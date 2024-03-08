
# Create a function that calculates the total marks 
def calc_marks(a,b,c,d,e):
    total_marks=a+b+c+d+e
    return(total_marks)


# Write a python program that takes from a user 5 inputs (maths, eng, swa, sci, sos). 
maths=float(input("enter marks:"))
eng=float(input("enter marks:"))
swa=float(input("enter marks:"))
sci=float(input("enter marks:"))
sos=float(input("enter marks:"))

total=calc_marks(maths,eng,swa,sci,sos)
print(total)

# # another the average marks 
def avg_marks(a,b):
    avg=(a)/5
    return avg

average=avg_marks(total,5)
print(average)


# then a functions that finds the grade according to the table below. 
# Use the value from total to get the average and average to find the grade.
# A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40

def find_grade(average):

    if average >= 79 :
        grade="A"    
    elif average >= 60 and average < 79:
        grade="B"
    elif average >= 59 and average <49:
        grade="C"
    else:
        grade="E"

    return(grade)

results=find_grade(average)
print(results)



 