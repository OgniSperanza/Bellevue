#Jacob Barnes
#Example Program that converts gallons to liters

def main():
    # display the intro screen.
    intro()
  
    try:  
        #Get number of gallons
        gallons = float(input("Enter the number of gallons: "))

        #Convert to liters
        gallonsToLiters(gallons)
    except:
      print("An execption occurred, try again by entering only a number...")
      print()
      main()

# The intro function displays an introductory screen.
def intro():
    print('This program converts gallons into liters.')
    print('For your reference the formula is:')
    print('1 gallon = 3.78541 liters')
    print()

# Convert the gallons to liters rounded to 2 decimal places.
def gallonsToLiters(gallons):
    liters = gallons * 3.78541
    print(f"That converts to {liters:.2f} liters.")    

  # Call the main function.
main()