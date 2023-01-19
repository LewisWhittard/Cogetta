import TranspositionCipherColumn
import CharacterSet
from random import *
import operator



class Table():
    def __init__(self,iD):
        self.CharacterSetClass = CharacterSet.TranspositionCipherKeySet
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
        GenaratedKey = self.CharacterSetClass.transpositionCipherColumnId.copy()
        shuffle(GenaratedKey)
        for i in GenaratedKey:
            if Counter == 7:
                Key = Key + str(i)
            else:
                Key = Key + str(i) + "-"
            Counter = Counter + 1
        self.GenaratedKey = Key
        print("Your transposition cipher Key is", Key)
        
    def ImportKey(self,KeyImport):
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
        
        messageRangeValues = []
        Counter = 0
        messageRangeValues.append(0)
        
        messageRangeValues.append(messageRangeValues[0] + listOfValues[0].MessageCount)
        messageRangeValues.append(messageRangeValues[1] + listOfValues[1].MessageCount)
        messageRangeValues.append(messageRangeValues[2] + listOfValues[2].MessageCount)
        messageRangeValues.append(messageRangeValues[3] + listOfValues[3].MessageCount)
        messageRangeValues.append(messageRangeValues[4] + listOfValues[4].MessageCount)
        messageRangeValues.append(messageRangeValues[5] + listOfValues[5].MessageCount)
        messageRangeValues.append(messageRangeValues[6] + listOfValues[6].MessageCount)
        messageRangeValues.append(messageRangeValues[7] + listOfValues[7].MessageCount)
        
        messageRangeList = [] 
        messageRange0 = range(messageRangeValues[0],messageRangeValues[1])
        messageRange1 = range(messageRangeValues[1],messageRangeValues[2])
        messageRange2 = range(messageRangeValues[2],messageRangeValues[3])
        messageRange3 = range(messageRangeValues[3],messageRangeValues[4])
        messageRange4 = range(messageRangeValues[4],messageRangeValues[5])
        messageRange5 = range(messageRangeValues[5],messageRangeValues[6])
        messageRange6 = range(messageRangeValues[6],messageRangeValues[7])
        messageRange7 = range(messageRangeValues[7],len(Message))
        
        messageRangeList.append(messageRange0)
        messageRangeList.append(messageRange1)
        messageRangeList.append(messageRange2)
        messageRangeList.append(messageRange3)
        messageRangeList.append(messageRange4)
        messageRangeList.append(messageRange5)
        messageRangeList.append(messageRange6)
        messageRangeList.append(messageRange7)
        
        counter = 0
        
        newList = []
        
        for i in listOfValues:
            newDataColumn = TranspositionCipherColumn.ColumnNumberID(counter,messageRangeList[counter],i.KeyId)
            newList.append(newDataColumn)
            counter = counter + 1
        
        for i in newList:
            i.ImportMessage(Message)
        
        newList.sort(key=operator.attrgetter('KeyId'))
        
        MessagePartList = []
        
        for i in newList:
            MessagePart = i.ReturnMessagePart()
            MessagePartList.append(MessagePart)
        
        messageList = []
        
        message0 = ""
        message1 = ""
        message2 = ""
        message3 = ""
        message4 = ""
        message5 = ""
        message6 = ""
        message7 = ""
        
        for i in MessagePartList:
            print(i)
            counter3 = 0
            for x in i:
                if (counter3 == 0):
                    message0 = message0 + x
                elif (counter3 == 1):
                    message1 = message1 + x
                elif (counter3 == 2):
                    message2 = message2 + x
                elif (counter3 == 3):
                    message3 = message3 + x
                elif (counter3 == 4):
                    message4 = message4 + x
                elif (counter3 == 5):
                    message5 = message5 + x
                elif (counter3 == 6):
                    message6 = message6 + x
                elif (counter3 == 7):
                    message7 = message7 + x
                    counter3 = 0
                counter3 = counter3 + 1
        
        FinalMessage = ""
        FinalMessage = FinalMessage + message0
        FinalMessage = FinalMessage + message1
        FinalMessage = FinalMessage + message2
        FinalMessage = FinalMessage + message3
        FinalMessage = FinalMessage + message4
        FinalMessage = FinalMessage + message5
        FinalMessage = FinalMessage + message6
        FinalMessage = FinalMessage + message7
        
        print(FinalMessage)
                
                
    def Decrypt(self,message):
        listOfColumnStructure = self.CreateListOfColumnStructure()
        self.AssignKeyToColumnStructure(listOfColumnStructure)
        self.AssignValueCount(listOfColumnStructure, message)
        self.ReconstructMessage(listOfColumnStructure,message)
        
        
        
        
            
        
                
                
        
            
    