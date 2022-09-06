import CharacterSet
from random import *
import string

class WheelGenarator():
    
    def __init__(self):
        self.CharacterSetClass = CharacterSet.EnglishStandard()
        self.GenaratedWheelKey = None
        self.WheelSize = self.CharacterSetClass.maxId
        
    def GenarateWheelKey(self):
        WheelKey = ""
        Counter = 0
        GenaratedWheelKey = self.CharacterSetClass.inputId.copy()
        shuffle(GenaratedWheelKey)
        for i in GenaratedWheelKey:
            if Counter == self.WheelSize:
                WheelKey = WheelKey + str(i)
            else:
                WheelKey = WheelKey + str(i) + "-"
            Counter = Counter + 1
        self.GenaratedWheelKey = WheelKey

class Wheel():
    
    
    
    def __init__(self,wheelID):
        self.CharacterSetClass = CharacterSet.EnglishStandard()
        self.ImportedWheelKey = []
        self.GenaratedWheelKey = None
        self.WheelId = wheelID
        self.WheelSize = self.CharacterSetClass.maxId
        self.TurnValue = None
        self.InternalCount = 0
        if self.WheelId == 0:
            self.TurnValue = 1
        else:
            self.TurnValue = ((self.WheelSize + 1) ** self.WheelId)
            print("Test",self.WheelId, self.WheelSize, self.TurnValue)
            
        print(self.TurnValue)
        
    
        
    def ImportWheelKey(self,WheelKeyImport):
        self.ImportedWheelKey = WheelKeyImport.split("-")
        self.ImportedWheelKey = list((map(int, self.ImportedWheelKey)))
        
    def EncryptChar(self, originalData):
        ResultPart0 = self.GetCharId(originalData)
        ResultPart1 = self.GetRandomId(ResultPart0)
        ResultPart2 = self.GetFinalChar(ResultPart1)
        self.Turn()
        print("Wheel Used",self.WheelId)
        return ResultPart2
    
    def GetCharId(self, data):
        CharecterSet = self.CharacterSetClass.inputValues.copy()
        Counter = 0
        Result = None
        for i in CharecterSet:
            if (data == i):
                Result = Counter
                break
            else:
                Counter = Counter + 1
        return Result
        
    def GetRandomId(self, data):        
        Result = None
        for x in range(data + 1):
            Result = self.ImportedWheelKey[x]
        return Result

   
    def Turn(self):
        self.InternalCount = self.InternalCount + 1
        if self.InternalCount == self.TurnValue:
            NewImportedWheelKey = []
            for i in self.ImportedWheelKey:
                LoopInt = i
                if (LoopInt == self.WheelSize):
                    NewImportedWheelKey.append(0);

                else:
                    ElseInt = i + 1
                    NewImportedWheelKey.append(ElseInt);

            self.ImportedWheelKey.clear()
            self.ImportedWheelKey = NewImportedWheelKey.copy()
            self.InternalCount = 0
            print("Turn",self.WheelId)
    
            
    
    def GetFinalChar(self, data):        
        CharecterSet = self.CharacterSetClass.inputValues.copy()
        Counter = 0
        Result = None
        for i in CharecterSet:
            if (Counter == data):
                Result = i
                break
            else:
                Counter = Counter + 1
        return Result
    
    def DecryptChar(self, originalData):
        ResultPart0 = self.GetCharId(originalData);
        ResultPart1 = self.GetRandomIdValue(ResultPart0);
        ResultPart2 = self.GetFinalChar(ResultPart1);
        self.Turn()
        return ResultPart2
    
    def GetRandomIdValue(self, data):
        IDSet = self.ImportedWheelKey.copy()
        
        Counter = 0
        for i in IDSet:
            if (i == data):
                Result = Counter
                break
            else:
                Counter = Counter + 1
        return Result

        

        
        
        
    
   
    
        
                
                
                
                
            
            
            
        