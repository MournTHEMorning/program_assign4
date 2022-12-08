"""CREATE.PY: Make resource through attributes given"""
inv=open("inventory.csv","a")

class Create:
    #intialize method - pass because not required for this class
    def __init__(self):
        pass

    #add -algorithm to create new entry
    def add(self,item_name,specimen,price,creator):
        new_entry=str("{},{},{},{}".format(item_name,specimen,price,creator))
        print(new_entry,type(new_entry))
        inv.write("\n"+new_entry)

    #in emergency case to close file
    def closeFile(self):
        inv.close()

    #in emergency case to open file, append version
    def openFile(self):
        inv=open("inventory.csv","a")

