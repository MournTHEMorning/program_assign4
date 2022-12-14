"""APPLICATION.PY: access point of other classes and user interaction"""
#The theme of the inventory system is a scientific, suspicious fridge. One can manage or view the contents of this strange refrigerator...
#Password for admin access(lowercase and underscore needed): sus_fridge2022
    #no password: only reading permissions involved

#importing modules to create, read,edit and delete information in inventory.csv
import create,read,edit,delete

#making objects to reference respective classes
createAccess=create.Create()
readAccess=read.Read()
editAccess=edit.Edit()
deleteAccess=delete.Delete()

#variables for readability
line="-----*-----"
breakLine=("-----*"*2)+"-----"

#run() - runs program
def run(isManager,username):
    menuLoop=True   #variable that makes loop continue
    while(menuLoop):
        print("WELCOME TO THE 'FRIDGE' - INVENTORY MENU:\n READ[R] || EDIT[E] || CREATE[C] || DELETE[DEL] || EXIT[EXIT]")
        #try block for menu
        try:
            user=input("Please input your option here: ").upper()
            print(breakLine*2)

            #menu choices
            #menu choice - READ
            if(user=="R"):
                searchList=[]
                #search input
                #note: This is very specific. Coded to not find anything similar. Spelling must be correct 
                print("Please indicate the type of search and type below [Minimum 2 searches]. ")
                search=" "
                while (search.upper()!="STOP"):
                    #tells user if they can escape loop
                    if(len(searchList)>=2):
                        print("Type 'stop' to begin searching with your selected filters")

                    search=input("SEARCH TYPES ||PRICE[P] or OTHER[O](codes,common_name,creator): ")

                    #searching for retail price
                    if(search.upper()=="PRICE" or search=="p" or search=="P"):
                        try:
                            search=input("Please ask for retail price here (e.g. 3.14,20,33.1): ")
                            if search.upper() == "STOP":
                                search=" " #user cannot stop here
                            else:
                                search=float(search)
                                searchList.append(search)

                        except:
                            print("Not applicible. Please try again")

                        finally: #to prevent float.upper() errors
                            search=" "

                    #searching for code, names, creator (anything in list as str type)
                    elif(search.upper()=="OTHER" or search=="o" or search=="O"):
                        search=input("Please type your query (name, code or creator) here:")
                        if search.upper()=="STOP":
                            search=" " #user cannot stop here
                        searchList.append(search)
                    
                    #invalid answer
                    elif(search.upper()!="STOP"):
                        print("Please select PRICE[P] or OTHER[O] as an option")

                    #makes user stay if less than 2 searches
                    if (len(searchList)<2):
                        search=""
                    print(breakLine)
                
                print(line,"\nYour searches were: {} \nIn the database, you have {} match(es) to your searches.".format(searchList,readAccess.search(searchList)))
                print("Returning to main menu...\n",breakLine*2)
            #menu choice - leave menu
            elif(user=="EXIT"):
                menuLoop=False #leaves loop, exits menu

            #specific for manager role - if password or not
            elif(user=="E" or user=="C" or user=="DEL"):
                #if the user is a resource manager
                if (isManager):
                    #menu choice - EDIT
                    if(user=="E"):
                        print("Name a characteristic of the data you want to edit. (i.e. Creator, price, code, name)\nSpelling and Case counts.")
                        query=input("Characteristic: ")
                        #""causes infinite search; this prevents this
                        if(query!=""):
                            #uses quickSearch to return indexes of the lists that has the characteristic of variable query
                            times=readAccess.quickSearch(query,True) 
                        #item does not exist in database
                        if (len(times)==0):
                            print("You cannot edit something that does not exist.")
                        #item exists in database
                        elif (len(times)>=1):
                            #if Item appears more than once
                            if len(times)>1:
                                print("Please write the code of the item you would like (Spelling and case counts).\nInput anything else to quit.")
                                specific_item=input("ITEM'S UNIQUE CHARACTERISTIC: ")
                                #returns specific code's list index in csv file in list form
                                item_index=readAccess.quickSearch(specific_item,True)
                                #get the numeric value of item's index by extracting it from list
                                item_index=item_index[0]
                                    
                            #item appears once
                            elif len(times)==1:
                                item_index=times[0]
                            
                            #item does not exist or user quits editing
                            else:
                                item_index=-10

                            #the item index exists. it should be more or equal to one because index zero is category line
                            if (item_index>=1):
                                print("What would you like to edit?: PRICE [P] || CREATOR[C]\nInput anything else to quit")
                                edit_quality=input("I would like to edit: ").upper()

                                #Will change for price
                                if (edit_quality=="P" or edit_quality=="PRICE"):
                                    user_edit=float(input("Please enter your edit here (float value): "))
                                    editAccess.change(item_index,2,user_edit)
                                    
                                #Will change creator
                                elif (edit_quality=="C" or edit_quality=="CREATOR"):
                                    user_edit=input("Please enter your edit here: ")
                                    if len(user_edit)>=1 and (user_edit!=""):
                                        editAccess.change(item_index,3,(user_edit)+"\n")

                                 #which will cause user to leave
                                else:
                                    pass

                    #menu choice - Create
                    elif(user=="C"):
                        #getting values from users                        
                        item_name=input("What is the item's common name?: ").capitalize()
                        #item_name should not be stop - key word in other menu
                        #see if item already exists. (len(readAccess etc. etc)==0 means nothing else like it in database) 
                            # There should be no duplicates
                        while (item_name=="Stop") or (len(readAccess.quickSearch(item_name,False))!=0):
                            print("This is not a valid or duplicate item. Please choose again.")
                            item_name=input("What is the item's common name?: ").capitalize()
                        specimen_num=input("Input 3 digit code for specimen name: ")
                        #checking the length of the code. It should be 3 digits
                        while(len(specimen_num)!=3):
                            print("Your specimen code is not 3 digits or not unique.\n"+line)
                            specimen_num=input("Input 3 digit code for specimen name: ")

                        #expected error if not a float value. try and catch will grab exception
                        price=float(input("What is the retail price of item? (i.e. 3.14, 12.4,5214.0): "))
                        
                        #makes specimen code name
                        #if you CAN take the first 3 charas of name
                        if(len(item_name)>=3):
                            speci_chara=item_name[:3]

                        #if you cannot
                        else:
                            speci_chara=item_name
                            #length of speci_character is not 3, add a zero
                            while(len(speci_chara)!=3):
                                speci_chara=speci_chara+"O"
                        #specimen code created
                        specimen=(speci_chara.upper()+"-"+str(specimen_num))        

                        #adding to Inventory
                        createAccess.add(item_name,specimen,price,username)

                    #menu choice - Delete
                    elif(user=="DEL"):
                        characteristic=input("Name a unique characteristic of the data you want to delete (i.e. Code): ")
                        #if the input is valid
                        if characteristic!="":
                            existingItem_index=readAccess.quickSearch(characteristic,True)
                        
                            #if the item exists only once
                            if len(existingItem_index)==1:
                                print("Are you sure you want to delete the following item?\n Type BURN (provide upper case, user!) to remove data from database.")
                                burn_this=input("So, do you wish to remove the data?: ")
                                #consent to burn data
                                if burn_this=="BURN":
                                    #since there will only be one item in this list, this is the index of that is needed in burn()
                                    deleteAccess.burn(existingItem_index[0])
                                    input()
                                else:
                                    print("Understood. Fires extinguished.")

                            #else, meaning item does not exist or exists more than once
                            else:
                                print("This item does not exists in database or exists more than once; therefore not unique.")

                    #END OF ADMIN MENU
                    #meaning user has quit their option or finished with admin settings
                    print("Returning to main menu...\n",breakLine*2)
                
                #if the user is not a resource manager
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

verify=input("Password: ")
if(verify=="sus_fridge2022"): #password is "sus_fridge2022", lowercase
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