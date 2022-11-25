class Column():
    def __init__(self, iD):
        self.ID = iD
        self.ListOfLetters = []
        
    def AddLetter(self,Letter):
        self.ListOfLetters.append(Letter)
        
    def ReturnListOfLetters(self):
        StringToReturn = ""
        for i in self.ListOfLetters:
            StringToReturn = StringToReturn + i
        return StringToReturn

class ColumnStructure():
    def __init__(self, iD):
        self.ID = iD
        self.KeyId = None
        self.MessageCount = None
        
    def ImportMessageCount(self,Count):
        self.MessageCount = Count
    
    def ImportKeyId(self, keyId):
        self.KeyId = keyId
    
    def PrintAll(self):
        print(self.ID, self.KeyId, self.MessageCount)

class ColumnNumberID():
    def __init__(self, iD,ListOfIds, keyId):
        self.ID = iD
        self.ListOfValues = []
        for i in ListOfIds:
            self.ListOfValues.append(i)
        self.KeyId = keyId
        
    def printAll(self):
        
            print(self.ID, self.KeyId, self.ListOfValues)
        
