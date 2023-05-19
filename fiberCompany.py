#Jacob Barnes
import locale
locale.setlocale( locale.LC_ALL, '' )

print("Welcome to Ficticious Company!")

rate = 0.87
companyName = input("What is your company name? ")
feetOfFiber = float(input("How many feet of fiber optic cable would you like to purchase? "))

match feetOfFiber:
    case 101 <= feetOfFiber <= 250:
        rate = 0.8
    case 251 <= feetOfFiber <= 500:
        rate = 0.7
    case feetOfFiber > 500:
        rate = 0.5

totalCost = feetOfFiber * rate

print("Company Name: ", companyName)
print("Total Cost: ", locale.currency(totalCost, grouping=True ))
