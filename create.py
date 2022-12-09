"""CREATE.PY: Make resource through attributes given"""
class Create:
    #intialize method - pass because not required for this class
    def __init__(self):
        pass

    #add -algorithm to create new entry
    def add(self,item_name,specimen,price,creator):
        inv=self.openFile()
        new_entry=str("{},{},{},{}".format(item_name,specimen,price,creator))
        inv.write("\n"+new_entry)
        self.closeFile(inv)


    #close file
    def closeFile(self,inv):
        inv.close()

    # open file, append version
    def openFile(self):
        return open("inventory.csv","a")

