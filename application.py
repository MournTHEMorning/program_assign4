"""APPLICATION.PY: access point of other classes"""
inv=open("inventory.csv","r")
#inv=open("inventory.txt","a")
#read=inv.split(",")

line="-----*-----"
breakLine=("-----*"*2)+"-----"

def run(isManager):
    loop=True   #variable that makes loop continue
    while(loop):
        print("WELCOME TO THE FRIDGE - INVENTORY MENU:\n READ[R] || EDIT[E] || CREATE[C] || DELETE[DEL] || EXIT[EXIT]")
        #try block for menu
        try:
            user=input("Please input your option here: ").upper()

            #menu choices
            #menu choice - READ
            if(user=="R"):
                print("read")

            #menu choice - leave menu
            elif(user=="EXIT"):
                loop=False #leaves loop, exits menu

            #specific for manager role - if password or not
            elif(user=="E" or user=="C" or user=="DEL"):
                if (isManager):
                    #menu choice - EDIT
                    if(user=="E" and isManager):
                        print("edit")

                    #menu choice - Create
                    elif(user=="C" and isManager):
                        print("create")

                    #menu choice - Delete
                    elif(user=="DEL" and isManager):
                        print("delete")
                else:
                    print("You do not have authorization")

            #menu choice - invalid if option not on menu
            else:
                print("Invalid Input - Please select a valid option")

    
        #except and finally block for menu
        except:
            print("Some error occured.")
        finally:
            print(line)

#weird as heck fridge
#Item,Specimen Name,Edible,Retail Price,Date(Month Day Year)
verify=input("Password: ")
if(verify=="aa"):
    certified=True #if certified to change or not
    print("cool")

else:
    certified=False #if certified to change or not
    print("this is the outside look")

run(certified)


print("Thank you! **PLEASE WASH HANDS 2.5 TIMES BEFORE LEAVING**")
inv.close()