from datetime import datetime

today=datetime.now()
dob=input("enter date of birth (dd/mm/yy):")
split_dob=dob.split("/")
print(split_dob)

year_dob=int(split_dob[2])
months_dob=int(split_dob[1])
days_dob=int(split_dob[0])

int_dob=datetime(day=days_dob,month=months_dob,year=year_dob)
age=today-int_dob
years=age.days//365
months=(age.days%365)//31
days=age.days%365%31

print(f"{years}:years,{months}:months,{days}:days")

