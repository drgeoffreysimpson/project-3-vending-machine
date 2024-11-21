
def loadInventory():
    #open the file and read the contents
    the_inventory = {}
    return the_inventory

def printMenu():
    print("Please choose from the following options:")
    print(" (d) Display items")
    print(" (p) Purchase item")
    print(" ($) Change currency")
    print(" (c) Generate inventory chart")
    print(" (q) Quit")

if __name__=="__main__":

    print("Welcome to the TU Vending Machine!")

    #load data from tu_vending_inventory.json and save into memory or database
    my_inventory = loadInventory()

    

    keepLooping = True
    runningSalesTotal = 0.0

    while(keepLooping):
        printMenu()
        user_input = input(">")
        #handle the user_input

    save