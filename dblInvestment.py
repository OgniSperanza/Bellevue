#Jacob Barnes

#Get the rate and initial investment
rate = float(input("Enter the interest rate as a whole number, e.g. '10%' as '10': "))
initialAmount = float(input("Enter the initial investment as a whole number, e.g. '$100' as '100': "))

#Calculate the years it takes to double
years = 0
currentAmount = initialAmount
while currentAmount < initialAmount * 2:
    currentAmount += currentAmount * (rate/100)
    years += 1
    #print("Year", years, ":", currentAmount)

#Print the # of years
print("It will take", years, "years to double the investment.")