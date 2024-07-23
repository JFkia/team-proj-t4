from inventory.inventory import Inventory
class ResourceCenter:
    def __init__(self):
        ## Prepare the data (Inventory list)
        self.inventory = Inventory()

    def display_menu(self):
        choice = -1
        while not 1 <= choice <= 5:
            print("\n==============================================")
            print('RESOURCE CENTRE SYSTEM by Chan Yi Chen')
            print("1. Add item")
            print("2. Display Inventory")
            print("3. Loan item")
            print("4. Return item")
            print("5. Quit")
            choice = int(input("Enter your choice >"))
            if not 1 <= choice <= 5:
                print("Invalid choice, please enter again.\n")
        return choice

    def main(self):
        # Refactor (A): Extract constants for choice integers
        choice_add = 1
        choice_display = 2
        choice_loan = 3
        choice_return = 4
        choice_quit = 5
        # Refactor (A): Extract constants for option integers
        option_camera = 1
        option_laptop = 2
        #### Menu driven application ####
        # Display menu and obtain menu choices
        choice = self.display_menu()

        while choice != choice_quit:

            if choice == choice_add:
                # Refactor (B): use printHeader(mesage)
                print("")
                print("==============================================")
                print("Add an item")
                print("==============================================")
                
                # Refactor (B): Extract duplicate codes to selectItemType(),
                # return the option selected.
                # Advance refactoring: error chekcing in selectItemType().
               

                print("\nItem types:")
                print("1. Digital Camera")
                print("2. Laptop")
                option = int(input("Enter option to select item type >"))

                # TO-DO: Write the code to ADD a digital camera or laptop.
                if option == option_camera:
                    assetTag = input("Enter asset tag >")
                    description = input("Enter descrition >")
                    opticalzoom = int(input("Enter optical zoom >"))
                    result = self.inventory.addCamera(assetTag, description, opticalzoom)
                    if result:
                        print("Digital camera added.")
                    else:
                        print("Error adding digital camera.")

                elif option == option_laptop:
                    assetTag = input("Enter asset tag >")
                    description = input("Enter descripion >")
                    os = input("Enter os >")
                    result = self.inventory.addLaptop(assetTag, description, os)
                    if result:
                        print("Laptop added.")
                    else:
                        print("Error adding laptop.") 
                else:
                    print("Invalid item type.")


            
            elif choice == choice_display:
                # Refactor (B): Extract duplicate codes to printHeader(message)
                print("")
                print("==============================================")
                print("Display all items")
                print("==============================================")

                # TO-DO: Write the code to display all digital camera or laptop.
                print(self.inventory.getNotAvailableCamera())
                print(self.inventory.getNotAvailableLaptop())


                
            elif choice == choice_loan:
                # Refactor (B): use printHeader(mesage)
                print("")
                print("==============================================")
                print("Loan an item")
                print("==============================================")
                
                # Refactor (B): use selectItemType()
                print("\nItem types:")
                print("1. Digital Camera")
                print("2. Laptop")
                option = int(input("Enter option to select item type >"))

                # TO-DO: Write the code to LOAN a camcorder or chrome book
                
            elif choice == choice_return:
                # Refactor (B): use printHeader(mesage)
                print("")
                print("==============================================")
                print("Return an item")
                print("==============================================")
                
                # Refactor (B): use selectItemType()
                print("\nItem types:")
                print("1. Digital Camera")
                print("2. Laptop")
                option = int(input("Enter option to select item type >"))

                # TO-DO: Write the code to RETURN a camcorder or chrome book

            else:
                print("Invalid choice.")
            
            choice = self.display_menu()

        print("Good bye.")

if __name__ == "__main__":
    app = ResourceCenter()
    app.main()