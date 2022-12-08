"""READ.PY: Find items that fit on two characteristics, at least. Basically like a google search"""
class Read:
    def __init__(self):
        print("This is READ")

    def updateList(self):
        self.invList=[] #list that represents data. Will iterate through
        inv=open("inventory.csv","r")
        for aLine in inv:
            self.invList.append(aLine.split(","))

        for database in range(len(self.invList)):
            if(database==0):
                continue
            else:
                self.invList[database][2]=float(self.invList[database][2])

        inv.close()
        return self.invList

    def search(self,search):
        invList=self.updateList()
        counter=0
        print(*invList[0],sep="  -  ")
        #entry = every list element in invList
        for entry in invList[1:]:
            #for every element in each list entry
            for elements in entry:
                #if search in list
                if(elements==search):
                    print(*entry,sep="  |  ")
                    counter+=1

        return ("There are {} entries in the database, and {} match to your search.".format(len(invList),counter))

    #in emergency case to close file
    def closeFile(self,inv):
        inv.close()

    #in emergency case to open file, read version
    def openFile(self):
        inv=open("inventory.csv","r")


print(Read().search("Aud"))