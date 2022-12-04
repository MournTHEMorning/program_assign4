"""USED FOR TESTING - TO BE DELETED"""

inv=open("inventory.csv","r")

counter=0
for aLine in inv:
   values=aLine.split(",") # now a list called values
   print(values)
   
   if (counter>=1):
    values[2]=bool(values[2]) #turning Edible into True/False
    values[3]=float(values[3]) #turning retail price to float

   counter+=1

   print(values,"\n -------------*********------")

inv.close()