"""USED FOR TESTING - TO BE DELETED"""

iRead=open("inventory.csv","r")
inv=open("inventory.csv","a")


#actually reads it; readline(CHARACTERS)
a=(list(iRead.read())) # this gives you ['I','t','e' ...] every character is an element in the list. 
print(len(a)) #250 characters as of dec 5th

testLi=["start",2321.23,["hi",True,3.24,"bye","okay"],True,["okay",3.24,"to-do"],"6",["find"],False,231.3,"end","\n"]
loop=True
"""
while loop:
    search=input("SEARCH TYPES || EDIBLE, PRICE, or OTHER(codes,creator,common_name): ")
    findEdible="Not Applicible"

    #searching for edible type
    if(search.capitalize()=="Edible"):
        specific=input("Item is edible: True or False?: ").capitalize()
        if (specific=="True"):
            findEdible=True
            loop=False

        elif(specific=="False"):
            findEdible=False
            loop=False

        #if it's edible option but NOT a true or false statement
        elif(search.capitalize()=="Edible" and (specific!="True" or specific!="False")):
            print("Invalid input. Please try again.")
            loop=True
        
    #searching for retail price
    elif(search.upper()=="PRICE" or search.upper()=="RETAIL PRICE" or search.upper()=="RETAIL_PRICE"):
        try:
            search=float(input("Please ask for retail price here: "))
            loop=False

        except:
            print("Not applicible. Please try again")
            loop=True
    
    elif(search.lower()=="other"):
        search=input("Please type your query here:")
        loop=False
    
    

counter=0
for words in testLi:
    print(words)
    if(type(words)==list):
        for elements in words:
            if(elements==search):
                print("FOUND IT!",elements,testLi.index(words))
                counter+=1
            elif(elements==findEdible and type(elements)==bool):
                print("FOUND IT! Elif!",elements,testLi.index(words))
                counter+=1

    
    elif(words==findEdible and type(words)==bool):
        print("FOUND IT! baha",words,testLi.index(words))
        counter+=1

    else:
        if(words==search):
            print("FOUND IT! doommm",words,testLi.index(words))
            counter+=1

print("out of {} entries: ".format(len(testLi)),counter,"of them had results of your search.")
"""

#Changing value types in values and putting it into variable
counter=0
var_inv=[]
for aLine in iRead:
    values=aLine.split(",") # now a list called values
    print(values)
    try:
        if (counter>=1):
            values[2]=bool(values[2]) #turning Edible into True/False
            values[3]=float(values[3]) #turning retail price to float
            var_inv.append(values) #will only have lists of the info, not titles

    except Exception as e:
        print(e)
        continue

    finally: 
        counter+=1
#    print(values,"\n -------------*********------")

# print(var_inv)

#testing how append works
# #this is how you'd do CREATE menu, but add parameters for each section (i.e. give me name, then code, etc.)
#user=input("Write something: ")

#if right format, then will be stored in var_inv for next bit
#RIGHT FORMAT: Item,Specimen-Name,Edible(bool),Retail-Price(float),Scientist-Name
#inv.write("\n"+user) #.write() needs file and requires string parameter; also add \n in front for next line



# #inv.write(str(var_inv)) #you don't need when doing append or it GETS FUNKY (like starts adding and adding in on itself)

#print(var_inv)


inv.close()
iRead.close()


#ORIGINAL DATA of inventory.csv
# Item,Specimen-Name,Edible,Retail-Price,Scientist-Name
# Orange,ORA-123,True,3.45,Aud
# Moss,MOS-346,False,123.26,Aud
# "Charlie",CHA-731,True,92.6,Aud
# Donut,DON-167,False,7000.07,Aud