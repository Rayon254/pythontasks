# Write a program that calculates the total stock in a company from the array/list below
#  if we know that the stock is the last digit in every array/list.





prods = [['omo','30kshs','300'], 
['milk','50kshs','200'],
['bread','45kshs','359'],
 ['','5kshs','79']['tea','100kshs','1000']]
total_stock=0

for i in prods:
    stk=int(i[2])
    total_stock=total_stock+stk
print(total_stock)




# stock=int(prods[0][2])+int(prods[1][2])+int(prods[2][2])+int(prods[3][2])
# print(stock)


