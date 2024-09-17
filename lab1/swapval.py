#Given two variables with values as shown below in the first two statements, 
#swap the values in the variables so that quantity holds the int value and 
#unitCost holds the float value.
quantity = 15.9
unitCost = 10
print("Quantity is:",quantity)
print("Unit Cost is:",unitCost)
print()

#Correct the following if you do not agree that this will give you the 
#correct results. 
tmp = unitCost

unitCost = quantity
quantity = tmp

print("Quantity is:",quantity)
print("Unit Cost is:",unitCost)