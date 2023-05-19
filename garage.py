#Jacob Barnes

class Vehicle:
    def setMake(self, make):
        self.make = make

    def setModel(self, model):
        self.model = model

    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

class Car(Vehicle):
    def setDoors(self, doors):
        self.doors = doors

    def getDoors(self):
        return self.doors


class Truck(Vehicle):
    def setBedLength(self, bedLength):
        self.bedLength = bedLength

    def getBedLength(self):
        return self.bedLength

vehicles = []

print("Welcome to Bellevue University Virtual Garage")
print("")
selection = 0
while int(selection) < int(4):
    selection = input("Enter 1 to make a car, 2 to make a truck, 3 to print current list of vehicles, or 4 to quit: ")
    print("")
    if (selection == '1'):
        newCar = Car()
        strMake = input("Please enter the car make: ")
        newCar.setMake(strMake)
        strModel = input("Please enter the car model: ")
        newCar.setModel(strModel)
        strDoors = input("Please enter the number of doors: ")
        newCar.setDoors(int(strDoors))
        vehicles.append(newCar)
        print("")
        print(f"The number of doors: {newCar.getDoors()}")
        print(f"The make is: {newCar.getMake()}")
        print(f"The model is: {newCar.getModel()}")
        print("You car has been added to the garage.")
    elif (selection == '2'):
        newTruck = Truck()
        strMake = input("Please enter the truck make: ")
        newTruck.setMake(strMake)
        strModel = input("Please enter the truck model: ")
        newTruck.setModel(strModel)
        strDoors = input("Please enter the bed length: ")
        newTruck.setBedLength(float(strDoors))
        vehicles.append(newTruck)
        print("")
        print(f"The bed length is: {newTruck.getBedLength()}")
        print(f"The make is: {newTruck.getMake()}")
        print(f"The model is: {newTruck.getModel()}")
        print("Your truck has been added to the garage.")
    elif (selection == '3'):
        for i, vehicle in enumerate(vehicles):
            print(f"Vehicle {i+1}: ")
            if isinstance(vehicle, Car):
                print(f"Type: Car")
                print(f"Doors: {vehicle.getDoors()}")
            elif isinstance(vehicle, Truck):
                print(f"Type: Truck")
                print(f"Bed Length: {vehicle.getBedLength()}")
            print(f"Make: {vehicle.getMake()}")
            print(f"Model: {vehicle.getModel()}")
            print("")        
    else:
        print("")
        print("Thank you for using the Bellevue University Garage.")
        print("")
