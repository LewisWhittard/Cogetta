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