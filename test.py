"""USED FOR TESTING - TO BE DELETED"""

iRead=open("inventory.csv","r")
inv=open("inventory.csv","a")

#Changing value types in values and putting it into variable
counter=0
var_inv=[]
for aLine in iRead:
    values=aLine.split(",") # now a list called values
    #print(values)
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
user=input("Write something: ")

#if right format, then will be stored in var_inv for next bit
#RIGHT FORMAT: Item,Specimen-Name,Edible(bool),Retail-Price(float),Scientist-Name
inv.write("\n"+user) #.write() needs file and requires string parameter; also add \n in front for next line



# #inv.write(str(var_inv)) #you don't need when doing append or it GETS FUNKY (like starts adding and adding in on itself)

print(var_inv)

inv.close()
iRead.close()


#ORIGINAL DATA of inventory.csv
# Item,Specimen-Name,Edible,Retail-Price,Scientist-Name
# Orange,ORA-123,True,3.45,Aud
# Moss,MOS-346,False,123.26,Aud
# "Charlie",CHA-731,True,92.6,Aud
# Donut,DON-167,False,7000.07,Aud