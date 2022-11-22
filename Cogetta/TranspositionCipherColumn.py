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