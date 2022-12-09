"""READ.PY: Find items that fit on two characteristics, at least. Basically like a google search"""
class Read:
    #intialize method - pass because not required for this class
    def __init__(self):
        pass

    #updateList - updates the list
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

        self.closeFile(inv)
        return self.invList

    #search - searches for requested search list items; very specific
    def search(self,searchList):
        invList=self.updateList()
        counter=0
        print(*invList[0],sep="  -  ")
        for search in searchList:
            #entry = every list element in invList
            for entry in invList[1:]:
                #for every element in each list entry
                for elements in entry:
                    #if last entry, this is the creator and \n is to be removed
                    if (entry.index(elements)==len(entry)-1):
                        elements=elements[0:-1]
                    #if search in list
                    if(elements==search):
                        print(*entry,sep="  |  ")
                        counter+=1

        return counter

    #quickSearch - searches for str query and gives indexCounter list of which line the element is in the list through indexCounter
    #used by the Delete and Edit classes
    def quickSearch(self,query):
        invList=self.updateList()
        indexCounter=[]

        #check counts if the len matches original string; checking is loop for if the search is a float or not
        check=0; checking=True
        while checking:
            try:
                for chara in query:
                    #decimal in case it is "16.7" or a float with decimal
                    if chara == ".":
                        check+=1
                    
                    #checking numbers
                    else:
                        for num in "1234567890":
                            if (chara == num):
                                check+=1
                #points == length; then all characters are available for float type
                if(len(query)==check):
                    query=float(query)
                checking=False

            except:
                continue

        print(*invList[0],sep="  -  ")
        for entry in invList[1:]:
            #for every element in each list entry
            for elements in entry:
                #if last entry, this is the creator and \n is to be removed
                if (entry.index(elements)==len(entry)-1):
                    elements=elements[0:-1]
                #if search in list
                if(elements==query):
                    print(*entry,sep="  |  ")
                    indexCounter.append(invList.index(entry))

        return indexCounter

    #read - Reads raw csv data
    def read(self):
        inv=open("inventory.csv","r")
        for aLine in inv:
            print(aLine)

        self.closeFile(inv)

    #icloseFile - to close file
    def closeFile(self,inv):
        inv.close()

    #openFile- to open file, read version
    def openFile(self):
        inv=open("inventory.csv","r")

#Testing ones - delete later
# print(Read().quickSearch("\"Charlie\""))
# print(Read().quickSearch("Aud"))
# print(Read().search("Jesus"))
# print(Read().search("Nothing"))
# print(Read().search(True))
# print(Read().search(3.14))
# print(Read().search(123.26))
# print(Read().search("\"Charlie\""))
# print(Read().search("Moss"))
# print(Read().search("MOS-346"))
# print(Read().search("CHA"))
# print(Read().search("ORA-123"))
# print(Read().search("READ"))
# print(Read().search("|"))
# print(Read().search("Retail-Price"))
# print(Read().search("Item"))