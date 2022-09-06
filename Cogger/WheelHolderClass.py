import WheelClass

class WheelHolder():
    
    
    def __init__(self):
        self.Wheels = []
    
    def GenarateKey(self, Number): 
        KeyList = []
        Key = ""
        for x in range(Number):
            self.Wheels.append(WheelClass.WheelGenarator());
        
        for x in range(Number):
            self.Wheels[x].GenarateWheelKey()
        
        Counter = 0
        for i in self.Wheels:
            if Counter == Number - 1:
                Key = Key + str(i.GenaratedWheelKey)
            else:
                Key = Key + str(i.GenaratedWheelKey) + "+"
            Counter = Counter + 1
        print(Key);
        
    def ImportKey(self, ImportedKey):
        Key = ImportedKey
        WheelKeyList = Key.split("+")
        WheelIdCounter = 0;
        for i in WheelKeyList:
            self.Wheels.append(WheelClass.Wheel(WheelIdCounter));
            WheelIdCounter = WheelIdCounter + 1;
        
        Counter = 0
        TempWheelList = []
        for i in WheelKeyList:
            self.Wheels[Counter].ImportWheelKey(i)
            Counter = Counter + 1
            
    def EncryptMessage(self, Message):
        FinalOutput = ""
        for i in Message:
            NewValue = i
            for x in self.Wheels:
                NewValue = x.EncryptChar(NewValue);
            FinalOutput = FinalOutput + NewValue
        print(FinalOutput)    

    def DecryptMessage(self, Message):
        FinalOutput = ""
        for i in Message:
            NewValue = i
            for x in reversed(self.Wheels):
                NewValue = x.DecryptChar(NewValue);
            FinalOutput = FinalOutput + NewValue
        print(FinalOutput)
    
        


    









           


