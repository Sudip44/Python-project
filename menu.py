fruits = ['apple','banana','orange','lemon']
print(" ********** Chose your action: ************* ")
print("1. View list")
print("2. Add item to the list")
print("3.Remove item for the list")
print("4.Exit")
#______________________________________________________________________#
def cont():
    ans = input("Do you want to continue(Y/N):")
    if(ans == 'Y' or ans == 'y'):
        choice()
def view():
    print(fruits)
    cont()
def addItem():
    item = input("enter the name of item: ")
    pos = input("enter the postion at which you want to insert item ( 0 = first position):")
    fruits.insert(int(pos),item)
    print("The new list is:")
    print(fruits)
    cont()
def deleteItem():
    item = input("which item you want to remove:")
    if item not in fruits:
        print("No such item present in list")
    else:
        fruits.remove(item)
    print("The new list is:")
    print(fruits)
    cont()
def end():
    print("Thank you for working with us...")
    print("..............Now exiting.........")
    
def choice():
    choice = int(input("enter your choice:"))
    if(choice==1):
        view()
    elif(choice == 2):
        addItem()
    elif( choice == 3):
        deleteItem()
    elif( choice == 4):
        end()
    else:
        print("Please select valid option")
choice()






    
    
