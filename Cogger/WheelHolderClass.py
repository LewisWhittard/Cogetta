import WheelClass

class WheelHolder():
    Wheels = []
    
    def GenarateKey(self, Number): 
        KeyList = []
        Key = ""
        for x in range(Number):
            self.Wheels.append(WheelClass.Wheel());
        
        for x in range(Number):
            self.Wheels[x].GenarateWheelKey()
        
        Counter = 0
        for i in self.Wheels:
            if Counter == Number - 1:
                Key = Key + str(i.GenaratedWheelKey)
                print(i);
            else:
                Key = Key + str(i.GenaratedWheelKey) + "+"
                print(i);
            Counter = Counter + 1
        print(Key);
        
    def ImportKey(self, ImportedKey):
        Key = ImportedKey
        WheelKeyList = Key.split("+")
        for i in WheelKeyList:
            self.Wheels.append(WheelClass.Wheel());
        
        Counter = 0
        TempWheelList = []
        for i in WheelKeyList:
            self.Wheels[Counter].ImportWheelKey(i)
            Counter = Counter + 1
            
    def EncryptMessage(self, Message):
      FinalOutput = ""
      Counter = 0
      for i in Message:
          NewValue = self.Wheels[Counter].EncryptChar(i);
          FinalOutput = FinalOutput + NewValue
          self.Wheels[Counter].PlusOneToId();
      print(FinalOutput)    

    def DecryptMessage(self, Message):
      FinalOutput = ""
      Counter = 0
      for i in Message:
          NewValue = self.Wheels[Counter].DecryptChar(i);
          FinalOutput = FinalOutput + NewValue
          self.Wheels[Counter].PlusOneToId();
      print(FinalOutput)

    def WheelTurnManager(self):
        WheelsToTurnList = [True]
        
        WheelCount = 0

        for i in self.Wheels:
            WheelCount = WheelCount + 1

        Counter = 0
        for i in self.Wheels:
            if (Counter == 0):
                self.Wheels[Counter].PlusOneToId();
            else:
                Number = Counter - 1
                if (self.Wheels[Number].ImportedWheelKey[0] == 0):
                    self.Wheels[Counter].PlusOneToId();
            Counter = Counter + 1
                




    def SingleCharEncryptionVersion2(self, Char):
        returnValue = Char
        Counter = 0
        for i in self.Wheels:
            returnValue = self.Wheels[Counter].EncryptChar(returnValue);
            self.WheelTurnManager();
            return returnValue

    def EncryptMessageVersion2(self, Message):
        FinalOutput = ""
        Counter = 0
        for i in Message:
          NewValue = self.SingleCharEncryptionVersion2(i)
          FinalOutput = FinalOutput + NewValue
        
        print(FinalOutput)
        for i in self.Wheels:
                i.PrintWheelContents()

    def SingleCharDecryptionVersion2(self, Char):
        returnValue = Char
        Counter = 0
        for i in reversed(self.Wheels):
            returnValue = self.Wheels[Counter].DecryptChar(returnValue);
            self.WheelTurnManager();
            return returnValue
    
    def DecryptMessageVersion2(self, Message):
        FinalOutput = ""
        Counter = 0
        for i in Message:
          NewValue = self.SingleCharDecryptionVersion2(i)
          FinalOutput = FinalOutput + NewValue
        
        print(FinalOutput)
        for i in self.Wheels:
                i.PrintWheelContents()
    
    
    
        


    









           


