"""DELETE.PY: Select resource by code and delete it from system"""

class Delete:
    #intialize method - pass because not required for this class
    def __init__(self):
        pass

    #burn - deletes data from database. "Burn" is the word that fits into the program's theme
    #del_index should be one int
    def burn(self,del_index):
        #recieving data
        readFile=self.openFileR()
        data=[]
        for aLine in readFile:
            data.append(aLine.split(","))

        self.closeFileR()
        try:
            #if there is data to delete in files and del_index is a number
            if len(data)>1 and type(del_index)==int:
                #rewrites file to include the changed data
                writeFile=self.openFileW()
                for line in data:
                    #+1 is to consider the category -- which is not a true line of data -- and should not be deleted
                    if data.index(line)==del_index:
                        continue
                    else:
                        writeFile.write(str("{},{},{},{}".format(*line)))
                
                self.closeFileW()
                print("Data and evidence burned. Removing debris... Hit any key to continue.")

            #Fail safe for not deleting categories    
            else:
                print("You do not have any data to delete.")

        except Exception as e:
            print("While deleting the data, an error appeared: ", e)
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

Delete().burn("hu")
Delete().burn(3)
Delete().burn(6)
# Item,Specimen-Name,Retail-Price,Scientist-Name
# Orange,ORA-123,3.45,Aud
# Moss,MOS-346,123.26,Aud
# "Charlie",CHA-731,92.6,Aud
# Donut,DON-167,7000.07,Aud
# Cup,CUP-136,326.4,Jesus
# Pickles,PIC-982,12.4,Two-seven-eight
# Luigi,LUI-907,999.99,Mario
# Juice,JUI-081,69.02,Login