"""CREATE.PY: Make resource through attributes given"""
inv=open("inventory.csv","a")

class Create:
    # #intiatilze method
    # def __init__(self):
    #     print("hey VSauce - create.py")

    #add -algorithm to create new entry
    def add(self,item_name,specimen,edibleStatus,price,creator):
        new_entry=str("{},{},{},{}".format(item_name,specimen,price,creator))
        print(new_entry,type(new_entry))
        inv.write("\n"+new_entry)

    #in emergency case to close file
    def closeFile(self):
        inv.close()

    #in emergency case to open file, append version
    def openFile(self):
        inv=open("inventory.csv","a")

