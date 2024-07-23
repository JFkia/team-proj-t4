from inventory.inventory import Inventory

class ResourceCenter:
    def __init__(self):
        self.inventory = Inventory()

def addCamera(self, assetTag, description, opticalzoom):
    correct = True
    if len(assetTag)== 0 or len(description) == 0 or opticalzoom<0:
        correct = False 
        error_message = "Incorrect values."
    
    notExist = True
    for c in self.cameraList:
        currentTag = c.getAssetTag()
        if currentTag == c.getassetTag:
            notExist = False
            error_message = "Asset already exist."
    
    if correct and notExist:
        new_camera = (assetTag, description, opticalzoom)
        self.cameraList.append(new_camera)
        return True
    else:
        print(error_message) 

def findAsset(self, assetTag):
    FoundAsset = None
    for c in self.cameraList:
        currentTag = c.getAssetTag()
        if currentTag == assetTag:
            FoundAsset = c
    for l in self.laptopList:
        currentTag = l.getAssetTag()
        if currentTag == assetTag:
            FoundAsset = 1
    return FoundAsset

def loanAsset(self, assertTag, dueDate):
    success = False
    if len(assertTag) > 0 and len(dueDate) > 0:
        foundAssert = self.findAssert(assertTag)
        if foundAssert != None:
            if foundAssert.getIsAvailable() == "Yes":
                foundAssert.setIsAvailable(False)
                foundAssert.setdueDate(dueDate)
                success = True
    return success
def loanCamera(self, assertTag, dueDate):
    return self.loanAsset(assertTag, dueDate)

def loanLaptop(self, assertTag, dueDate):
    return self.loanAsset(assertTag, dueDate)

def display_menu(self):
    choice = -1
    while not 1 <= choice <= 5:
        print("\n==============================================")
        print('RESOURCE CENTRE SYSTEM by Team 4')
        print("1. Add item")
        print("2. Display Inventory")
        print("3. Loan item")
        print("4. Return item")
        print("5. Quit")
        choice = int(input("Enter your choice >"))
        if not 1 <= choice <= 5:
            print("Invalid choice, please enter again.\n")
    return choice

def printHeader(self, message):
    print("\n==============================================")
    print(message)
    print("==============================================")

def select_item_type(self):
    print("\nItem types:")
    print("1. Digital Camera")
    print("2. Laptop")
    option = int(input("Enter option to select item type >"))
    return option

def add_item(self):
    self.printHeader("Add an item")
    option = self.select_item_type()
    if option == 1:  # Digital Camera
        asset_tag = input("Enter asset tag >")
        description = input("Enter description >")
        optical_zoom = int(input("Enter optical zoom >"))
        result = self.inventory.addCamera(asset_tag, description, optical_zoom)
        if result:
            print("Digital camera added.")
        else:
            print("Error adding digital camera.")
    elif option == 2:  # Laptop
        asset_tag = input("Enter asset tag >")
        description = input("Enter description >")
        os = input("Enter os >")
        result = self.inventory.addLaptop(asset_tag, description, os)
        if result:
            print("Laptop added.")
        else:
            print("Error adding laptop.")
    else:
        print("Invalid item type.")

def loan_item(self):
    self.printHeader("Loan an item")
    option = self.select_item_type()
    # TO-DO: Implement loan item functionality

def return_item(self):
    self.printHeader("Return an item")
    option = self.select_item_type()
    # TO-DO: Implement return item functionality

def main(self):
    choice_add = 1
    choice_display = 2
    choice_loan = 3
    choice_return = 4
    choice_quit = 5

    choice = self.display_menu()

    while choice != choice_quit:
        if choice == choice_add:
            self.add_item()
        elif choice == choice_display:
            self.display_inventory()
        elif choice == choice_loan:
            self.loan_item()
        elif choice == choice_return:
            self.return_item()
        else:
            print("Invalid choice.")

        choice = self.display_menu()

    print("Goodbye.")

if __name__ == "__main__":
    app = ResourceCenter()
    app.main()
