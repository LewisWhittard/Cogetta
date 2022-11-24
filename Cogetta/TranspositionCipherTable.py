import TranspositionCipherColumn
import CharacterSet
from random import *


class Table():
    def __init__(self,iD):
        self.CharacterSetClass = self.CharacterSetClass = CharacterSet.EnglishStandard()
        self.ID = iD
        self.ListOfColumns = []
        self.Key = None
        self.Column0 = TranspositionCipherColumn.Column(0)
        self.Column1 = TranspositionCipherColumn.Column(1)
        self.Column2 = TranspositionCipherColumn.Column(2)
        self.Column3 = TranspositionCipherColumn.Column(3)
        self.Column4 = TranspositionCipherColumn.Column(4)
        self.Column5 = TranspositionCipherColumn.Column(5)
        self.Column6 = TranspositionCipherColumn.Column(6)
        self.Column7 = TranspositionCipherColumn.Column(7)
        self.ListOfColumns.append(self.Column0)
        self.ListOfColumns.append(self.Column1)
        self.ListOfColumns.append(self.Column2)
        self.ListOfColumns.append(self.Column3)
        self.ListOfColumns.append(self.Column4)
        self.ListOfColumns.append(self.Column5)
        self.ListOfColumns.append(self.Column6)
        self.ListOfColumns.append(self.Column7)
        self.ImportedKey = None
        
    def importKey(key):
        Key = key
    
    def GenarateKey(self):
        Key = ""
        Counter = 0
        GenaratedKey = self.CharacterSetClass.transporationCipherColumnId.copy()
        shuffle(GenaratedKey)
        for i in GenaratedKey:
            if Counter == 7:
                Key = Key + str(i)
            else:
                Key = Key + str(i) + "-"
            Counter = Counter + 1
        self.GenaratedKey = Key
        print("Your transposition cipher Key is", Key)
        
    def ImportWheelKey(self,KeyImport):
        self.ImportedKey = KeyImport.split("-")
        self.ImportedKey = list((map(int, self.ImportedKey)))
    
    def EncryptMessage(self,message):
        counter = 0
        for i in message:
            currentId = self.ImportedKey[counter]
            for x in self.ListOfColumns:
                if (currentId == x.ID):
                    x.AddLetter(i)
            if counter == 7:
                counter = 0
            else:
                counter = counter + 1
        messageToPrint = ""
        for i in self.ListOfColumns:
            messageToPrint = messageToPrint + i.ReturnListOfLetters()
        return messageToPrint
    
    def CreateListOfColumnStructure(self):
        listOfColumnStructure = []
        ColumnStructure0 = TranspositionCipherColumn.ColumnStructure(0)
        ColumnStructure1 = TranspositionCipherColumn.ColumnStructure(1)
        ColumnStructure2 = TranspositionCipherColumn.ColumnStructure(2)
        ColumnStructure3 = TranspositionCipherColumn.ColumnStructure(3)
        ColumnStructure4 = TranspositionCipherColumn.ColumnStructure(4)
        ColumnStructure5 = TranspositionCipherColumn.ColumnStructure(5)
        ColumnStructure6 = TranspositionCipherColumn.ColumnStructure(6)
        ColumnStructure7 = TranspositionCipherColumn.ColumnStructure(7)
        listOfColumnStructure.append(ColumnStructure0)
        listOfColumnStructure.append(ColumnStructure1)
        listOfColumnStructure.append(ColumnStructure2)
        listOfColumnStructure.append(ColumnStructure3)
        listOfColumnStructure.append(ColumnStructure4)
        listOfColumnStructure.append(ColumnStructure5)
        listOfColumnStructure.append(ColumnStructure6)
        listOfColumnStructure.append(ColumnStructure7)
        return listOfColumnStructure
    
    def AssignKeyToColumnStructure(self, listOfValues):
        counter= 0
        for i in listOfValues:
            i.ImportKeyId(self.ImportedKey[counter])
            counter = counter + 1
            
    def GetCountValuesBasedOnId(self,ID):
        value = None
        for x in self.ListOfColumns:
            if (x.ID == ID):
                value = len(x.ListOfLetters)
                
        return value
    
    def AssignValueCount(self, listOfValues,message):
        counter = 0
        for i in message:
            currentId = self.ImportedKey[counter]
            for x in self.ListOfColumns:
                if (currentId == x.ID):
                    x.AddLetter(i)
            if counter == 7:
                counter = 0
            else:
                counter = counter + 1
        
        values = []
        
        for i in listOfValues:
            values.append(i.KeyId)
        
        Counter2 = 0    
        
        for i in values:
            listOfValues[Counter2].MessageCount = self.GetCountValuesBasedOnId(listOfValues[i].KeyId)
            Counter2 = Counter2 + 1
            
    def ReconstructMessage(self,listOfValues,Message):
        
        messageRange = []
        Counter = 0
        messageRange.append(0)
        
        messageRange.append(messageRange[0] + listOfValues[0].MessageCount)
        messageRange.append(messageRange[1] + listOfValues[1].MessageCount)
        messageRange.append(messageRange[2] + listOfValues[2].MessageCount)
        messageRange.append(messageRange[3] + listOfValues[3].MessageCount)
        messageRange.append(messageRange[4] + listOfValues[4].MessageCount)
        messageRange.append(messageRange[5] + listOfValues[5].MessageCount)
        messageRange.append(messageRange[6] + listOfValues[6].MessageCount)
        messageRange.append(messageRange[7] + listOfValues[7].MessageCount)
        
    def Decrypt(self,message):
        listOfColumnStructure = self.CreateListOfColumnStructure()
        self.AssignKeyToColumnStructure(listOfColumnStructure)
        self.AssignValueCount(listOfColumnStructure, message)
        self.ReconstructMessage(listOfColumnStructure,message)
        
        
        
            
        
                
                
        
            
    