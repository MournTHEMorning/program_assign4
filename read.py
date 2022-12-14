"""READ.PY: Find items that fit on two or more characteristics"""
class Read:
    #intialize method - pass because not required for this class
    def __init__(self):
        pass

    #updateList - updates the list; critical to get information
    def updateList(self):
        self.invList=[] #list that represents data. Will iterate through
        inv=open("inventory.csv","r")
        #for every line in inventory.csv, add it to the list
        for aLine in inv:
            self.invList.append(aLine.split(","))

        #change the database list for float values (allows for proper decimal searches)
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
    def quickSearch(self,query,showResults):
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
        #showResults- if the respective stats should be shown or not
        if(showResults): 
            print(*invList[0],sep="  -  ")
        for entry in invList[1:]:
            #for every element in each list entry
            for elements in entry:
                #if last entry, this is the creator and \n is to be removed
                if (entry.index(elements)==len(entry)-1):
                    elements=elements[0:-1]
                #if search in list
                if(elements==query):
                    indexCounter.append(invList.index(entry))
                    #showResults- if the respective stats should be shown or not
                    if(showResults): 
                        print(*entry,sep="  |  ")

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
        return open("inventory.csv","r")