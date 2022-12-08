"""APPLICATION.PY: access point of other classes"""
#importing modules to create, read,edit and delete information in inventory.csv
import create,read,edit,delete

#making objects to reference respective classes
createAccess=create.Create()
readAccess=read.Read()
# editAccess=edit
# deleteAccess=delete

#opening inventory.csv
invRead=open("inventory.csv","r")
invAppend=open("inventory.csv","a")
#read=inv.split(",")

#variables for readability
line="-----*-----"
breakLine=("-----*"*2)+"-----"

def run(isManager,username):
    menuLoop=True   #variable that makes loop continue
    while(menuLoop):
        print("WELCOME TO THE 'FRIDGE' - INVENTORY MENU:\n READ[R] || EDIT[E] || CREATE[C] || DELETE[DEL] || EXIT[EXIT]")
        #try block for menu
        try:
            user=input("Please input your option here: ").upper()

            #menu choices
            #menu choice - READ
            if(user=="R"):
                readLoop=True
                while readLoop:
                    search=input("SEARCH TYPES ||PRICE or OTHER(codes,creator,common_name): ")

                    #searching for retail price
                    if(search.upper()=="PRICE" or search.upper()=="RETAIL PRICE" or search.upper()=="RETAIL_PRICE"):
                        try:
                            search=float(input("Please ask for retail price here: "))
                            readLoop=False

                        except:
                            print("Not applicible. Please try again")
                            readLoop=True
                    #searching for code, names, creator (anything in list as str type)
                    elif(search.lower()=="other"):
                        search=input("Please type your query here:")
                        readLoop=False

                print(readAccess.search(search))

            #menu choice - leave menu
            elif(user=="EXIT"):
                menuLoop=False #leaves loop, exits menu

            #specific for manager role - if password or not
            elif(user=="E" or user=="C" or user=="DEL"):
                if (isManager):
                    #menu choice - EDIT
                    if(user=="E" and isManager):
                        print("edit")

                    #menu choice - Create
                    elif(user=="C" and isManager):
                        #getting values from users                        
                        item_name=input("What is the item's common name?: ").capitalize()
                        specimen_num=input("Input 3 digit code for specimen name: ")
                        #checking the length of the code. It should be 3 digits
                        while(len(specimen_num)!=3):
                            print("Your specimen code is not 3 digits.\n"+line)
                            specimen_num=input("Input 3 digit code for specimen name: ")

                        price=float(input("What is the retail price of item? (i.e. 3.14, 12.4,5214.0): "))
                        
                        #makes specimen code name
                        #if you CAN take the first 3 charas of name
                        if(len(item_name)>=3):
                            speci_chara=item_name[:3]

                        #if you cannot
                        else:
                            speci_chara=item_name
                            while(len(speci_chara)!=3):
                                speci_chara=speci_chara+"O"
                        #specimen code created
                        specimen=(speci_chara.upper()+"-"+str(specimen_num))        

                        #adding to Inventory
                        createAccess.add(item_name,specimen,price,username)

                    #menu choice - Delete
                    elif(user=="DEL" and isManager):
                        print("delete")
                else:
                    print("You do not have authorization")

            #menu choice - invalid input, if the option is not on menu
            else:
                print("Invalid Input - Please select a valid option")

        #except and finally block for menu
        except Exception as e:
            print("Some error occured: ",e)
        finally:
            print(breakLine)



#THEME: weird as heck fridge, kinda omnious but quirky
#Item,Specimen Name(FIRST THREE LETTERS OF IT-RANDOM NUM),Edible,Retail Price,Scientist Name(i.e. Aud,Harrison,Mario,dr.Ken,bob)
verify=input("Password: ")
if(verify=="aa"): #password is "aa", lowercase
    name=input("Correct. What is your name?: ").capitalize()
    print("You have recieved ADMIN access. Reminder to put on 20.3 masks in Style 10.\n"+line)
    certified=True #if certified to have admin access or not
else:
    certified=False 
    print("You have recieved GUEST access. Reminder to put on 10.4 masks in Style 16.\n"+line)
    name=""

print("**REMINDER: Please put on your gloves before proceeding**\n"+breakLine)
run(certified,name) #runs program 

#ending print statement
print(breakLine+"\nThank you! **REMOVE GLOVES & PLEASE WASH HANDS 2.5 TIMES BEFORE LEAVING**")

#closing inventory.csv
invRead.close()
invAppend.close()