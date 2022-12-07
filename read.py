"""READ.PY: Find items that fit on two characteristics, at least. Basically like a google search"""
inv=open("inventory.csv","r")

class Read:
    def __init__(self):
        print("This is READ")

    def updateList(self):
        self.invList=[] #list that represents data. Will iterate through
        for aLine in inv:
            section=inv.read().split(",") #HERE. TRY THIS


    def search(self):
        print("...I AM SEARCHINNGGG!!! SEARCHINGGGGG!!")

    #in emergency case to close file
    def closeFile(self):
        inv.close()

    #in emergency case to open file, read version
    def openFile(self):
        inv=open("inventory.csv","r")