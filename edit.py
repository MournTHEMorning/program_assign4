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

        data[listIndex][elementIndex]=newVal
        self.closeFileR()

        #rewrites file to include the changed data
        writeFile=self.openFileW()
        for line in data:
            writeFile.write(str("{},{},{},{}".format(*line)))

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

#Raw tester data:
# Item,Specimen-Name,Retail-Price,Scientist-Name
# Orange,ORA-123,3.45,Aud
# Moss,MOS-346,123.26,Aud
# "Charlie",CHA-731,92.6,Aud
# Donut,DON-167,7000.07,Aud
# Cup,CUP-136,326.4,Jesus
# Pickles,PIC-982,12.4,Two-seven-eight
# Luigi,LUI-907,999.99,Mario
# Juice,JUI-081,69.02,Login