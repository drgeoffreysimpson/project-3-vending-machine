# While this file contains a good deal of framework for the project, it is not 
# sufficient for the completion of the tasks.  Functions will need to be created,
# parameters passed, functions may need to return things, imports will have to be added,
# those kinds of things.   

def loadInventory():
    """Open the inventory file and read the JSON contents"""
    the_inventory = {}
    return the_inventory

def printMenu():
    """Helper function to print the menu"""
    print("Please choose from the following options:")
    print(" (d) Display items")
    print(" (p) Purchase item")
    print(" ($) Change currency")
    print(" (c) Generate inventory chart")
    print(" (q) Quit")
    pass

def displayInventory(my_inventory):
    """Prints the inventory to the screen"""
    #print the inventory to the screen
    print("----Current vending machine inventory-----")
    #print the inventory here.
    print("------------------------------------------")
    pass

def decrementInventory(my_inventory, slot_id):
    """decrement the inventory item associated with the slot_id"""
    #what happens if they try to decrement an item with zero inventory?
    pass

def saveTransaction(my_inventory, slot_id):
    """record a transaction for the slot_id item. """
    pass

def saveEndingInventory(my_inventory):
    """write inventory to file or database"""
    pass

if __name__=="__main__":

    print("Welcome to the TU Vending Machine!")

    #load data from tu_vending_inventory.json and save into memory or database
    my_inventory = loadInventory()
    keepLooping = True
    runningSalesTotal = 0.0

    while(keepLooping):
        printMenu()
        user_input = input(">").upper().strip()
        #handle the user_input
        if (user_input == "D"):
            displayInventory(my_inventory)
        elif (user_input == "Q"):
            keepLooping = False

    saveEndingInventory(my_inventory)