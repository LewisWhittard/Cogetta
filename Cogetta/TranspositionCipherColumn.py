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
    def _init_(self, iD):
        self.ID = iD
        self.KeyId = None
        self.MessageCount = None
        
    def ImportMessageCount(self,Count)
        self.MessageCount = Count
    
    def ImportKeyId(self, iD):
        self.KeyId = iD