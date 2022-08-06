import CharacterSet
from random import *
import string

class Wheel():
    def __init__(self):
        self.CharacterSetClass = CharacterSet.EnglishStandard()
        self.ImportedWheelKey = []
        self.GenaratedWheelKey = None
        self.WheelSize = self.CharacterSetClass.maxId
        
    def ImportWheelKey(self,WheelKeyImport):
        self.ImportedWheelKey = WheelKeyImport.split("-")
        self.ImportedWheelKey = list((map(int, self.ImportedWheelKey)))
        
    def GenarateWheelKey(self):
        WheelKey = ""
        Counter = 0
        GenaratedWheelKey = self.CharacterSetClass.inputId.copy()
        shuffle(GenaratedWheelKey)
        for i in GenaratedWheelKey:
            if Counter == 93:
                WheelKey = WheelKey + str(i)
            else:
                WheelKey = WheelKey + str(i) + "-"
            Counter = Counter + 1
        print (WheelKey)
        self.GenaratedWheelKey = WheelKey
        
    def EncryptChar(self, originalData):
        ResultPart0 = self.GetCharId(originalData);
        ResultPart1 = self.GetRandomId(ResultPart0);
        ResultPart2 = self.GetFinalChar(ResultPart1);
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

        

        
        
        
    
   
    
        
                
                
                
                
            
            
            
        