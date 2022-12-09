"""EDIT.PY: Edit resource by unique characteristic"""

class Edit:
    #intializer - not required for this class
    def __init__(self):
        pass

    #changes specific element given
    def change(self,listIndex,elementIndex,newVal):
        readFile=self.openFileR()
        data=[]
        for aLine in readFile:
            data.append(aLine.split(","))

        #changing creator, which is elementIndex, which would be index 3 or length of list -1 and needs \n at end
        if elementIndex==(len(data[0])-1):
            data[listIndex][elementIndex]=(newVal)

        #changing price
        else:
            data[listIndex][elementIndex]=newVal
        self.closeFileR()

        #rewrites file to include the changed data
        writeFile=self.openFileW()
        for line in data:
            writeFile.write(str("{},{},{},{}".format(*line)))
        
        print("Editing File: Update successful")
        self.closeFileW()


    #opens file read
    def openFileR(self):
        self.invRead= open("inventory.csv","r")
        return self.invRead
        
    #opens file write
    def openFileW(self):
        self.invWrite= open("inventory.csv","w")
        return self.invWrite
    #closes file read
    def closeFileR(self):
        self.invRead.close()
    
    #closes file write
    def closeFileW(self):
        self.invWrite.close()

#Test cases
# Edit().change(3,2,3.2)