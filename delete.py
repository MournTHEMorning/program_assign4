"""DELETE.PY: Select resource by code and delete it from system"""

class Delete:
    #intialize method - pass because not required for this class
    def __init__(self):
        pass

    #burn - deletes data from database. "Burn" is the word that fits into the program's theme
    def burn(self,del_index):
        #recieving data
        readFile=self.openFileR()
        data=[]
        for aLine in readFile:
            data.append(aLine.split(","))

        #rewrites file to include the changed data
        writeFile=self.openFileW()
        for line in data:
            if data.index(line)==del_index:
                pass
            else:
                writeFile.write(str("{},{},{},{}".format(*line)))
        
        print("Data and evidence burned. Removing debris... Hit any key to continue.")
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