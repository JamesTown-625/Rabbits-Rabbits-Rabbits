"""
1. Print a table that contains the following information for the beginning of each month.
    The number of months that have passed.
    The number adult rabbit pairs (those over 1 month old).
    The number of baby rabbits pairs produced this month.
    The total number of rabbit pairs in the lab.
2. Calculate how many months it will take until the number of rabbits exceeds the number of available cages.
3. Stop printing when you run out of cages.
4. Print a message giving how many months it will take to run out of cages
"""

print("\nTable of rabbit pairs\n")
#Print the table header row
headerArray = ['Month', 'Adults', 'Babies', 'Total']
for item in headerArray:
    print(item+"\t", end="")

#Initiate all variables in play for the 
cages = 500
month = 1
adult = 1
babies = 0
total = 1

#While loop that continues until total rabbits exceed available cages
while total < cages and cages != 0:
    total = adult + babies
    print("\n"+str(month), end="")
    print("\t"+str(adult), end="")
    print("\t"+str(babies), end="")
    print("\t"+str(total), end="")
    month = month + 1
    babies = adult
    adult = total

#Print the final number of months it will take to run out of cages
print("\n\nIt will take "+str(month-1)+" months to run out of cages!")
    
    
    