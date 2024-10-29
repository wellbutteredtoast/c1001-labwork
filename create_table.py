noOfRows = 5 #Table should have 5 rows
noOfCols = 3 #Table should have 3 columns

#Create an empty list
myList = []

noOfRows = 5 #with 5 rows
noOfCols = 3 #and 3 columns

#Enter the data values row-wise
for row in range(noOfRows - 1):  #for each row in range 0 - 4
    t_row = []
    for col in range(noOfCols - 1):
        val = int(input("Enter an int: "))
        t_row.append(val)
    myList.append(t_row)
        

print()
print("The following is the two dimensional list:")
print("The values of the list are: ", myList) 

#Print the values of the second row
print ("The values of the second row are:", myList[1])

#Print the values by columns 
print("Values printed by columns")
for col in range():
    print(" | ", end="")
    for row in range():
        print(..., end=" | ")
    print()